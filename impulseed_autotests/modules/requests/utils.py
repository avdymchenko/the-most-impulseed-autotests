import copy
import json
import re
import time
from functools import wraps
from typing import Any, Callable, Dict, Type

import requests
from requests import Response
from requests.exceptions import RequestException

from impulseed_autotests.modules.logging.custom_logger import get_logger

credentials_pattern = re.compile(r'username=(?P<username>\w+)&password=(?P<password>\w+)')


def request_func_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def func_wrapper(*args: Any, **kwargs: Any) -> Any:
        kwargs['verify'] = False
        return func(*args, **kwargs)
    return func_wrapper


def __replace_kwargs(kwargs: Dict[str, Any]) -> Dict[str, Any]:
    kwargs_ = copy.deepcopy(kwargs)
    data = kwargs_.get('data', None)
    if data and isinstance(data, str):
        credentials = credentials_pattern.search(data)
        if credentials:
            credentials = credentials.groupdict()
            kwargs_['data'] = kwargs_['data'].replace(credentials['username'], '***')
            kwargs_['data'] = kwargs_['data'].replace(credentials['password'], '***')
    params = kwargs_.get('params', None)
    files = kwargs_.get('files', None)
    if files:
        kwargs_['files'] = 'truncated'
    if params:
        kwargs_['params'] = {k: v for k, v in params.items() if v}
    headers = kwargs_.get('headers', None)
    if headers:
        if 'Authorization' in headers:
            kwargs_['headers']['Authorization'] = '***'
    return kwargs_


def retry_on_requests_exception(
        *,
        exception: Type[RequestException] = RequestException,
        retries: int = 3,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    log = get_logger(f'RequestsUtils[RetryOn{exception.__name__}]')

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            args_ = args[1:]
            kwargs_ = __replace_kwargs(kwargs)
            args_and_kwargs = []
            if args_:
                args_and_kwargs.append(str(args_))
            if kwargs_:
                args_and_kwargs.append(str(kwargs_))
            args_and_kwargs = ' и '.join(args_and_kwargs) if args_and_kwargs else None
            exception_ = None
            for i in range(retries):
                log.info(
                    'Попытка №%s выполнить функцию requests.%s '
                    'с аргументами: %s',
                    i + 1,
                    func.__name__,
                    args_and_kwargs,
                )
                try:
                    result = func(*args, **kwargs)
                except exception as e:
                    log.warning('Было поймано исключение: %s', e)
                    exception_ = e
                    time.sleep(30)
                    continue
                else:
                    log.info('Функция requests.%s была успешно выполнена', func.__name__)
                    return result
            else:
                raise exception_
        return wrapper
    return decorator


def retry_on_bad_request(
        retries: int = 3,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    log = get_logger('RequestsUtils[RetryOnBadRequest]')

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            exception_ = None
            for i in range(retries):
                log.info('Попытка №%s выполнить функцию %s', i + 1, func.__name__)
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    log.warning('Было поймано исключение: %s', e)
                    exception_ = e
                    time.sleep(30)
                    continue
                else:
                    log.info('Функция %s была успешно выполнена', func.__name__)
                    return result
            else:
                raise exception_
        return wrapper
    return decorator


def __replace_key_in_response_text(response_text: str, *, key: str) -> str:
    if key in response_text:
        response_json = json.loads(response_text)
        response_json[key] = '...'
        response_text = json.dumps(response_json)
    return response_text


def __prepare_response_text(response_text: str) -> str:
    response_text = __replace_key_in_response_text(response_text, key='access_token')
    response_text = __replace_key_in_response_text(response_text, key='refresh_token')
    if len(response_text) > 1000:
        response_text = f'{response_text[:1000]} ...'
    return response_text


def log_response_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    log = get_logger('RequestsUtils[LogResponse]')

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        response: Response = func(*args, **kwargs)
        status_code = str(response.status_code)
        log_method = log.info if status_code.startswith('2') else log.error
        log_method('В результате запроса вернулся статус-код: %s', status_code)
        response_text = __prepare_response_text(response.text)
        log_method('Текст ответа: %s', response_text or '<none>')
        return response

    return wrapper


def wrap_requests() -> None:
    methods = ('request', 'get', 'post', 'delete', 'put')
    for method_name in methods:
        for decorator in (log_response_decorator, request_func_decorator):
            method = getattr(requests, method_name)
            setattr(requests, method_name, decorator(method))
    for method_name in methods:
        method = getattr(requests.Session, method_name)
        setattr(
            requests.Session,
            method_name,
            retry_on_requests_exception()(method),
        )

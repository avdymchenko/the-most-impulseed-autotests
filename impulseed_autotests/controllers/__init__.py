from typing import Iterable

from httpx import Response

from impulseed_autotests.asserts import assert_in
from impulseed_autotests.model import ImpulseedAPI


class AdapterMixin:
    ERROR_MSG = 'В результате выполнения запроса вернулся некорректный код ответа'

    def assert_status_code_is_ok(
        self,
        response: Response,
        *,
        msg: str | None = None,
    ):
        self.assert_status_code_is_expected(
            response=response,
            expected_status_code=range(200, 209),
            msg=msg,
        )

    def assert_status_code_is_expected(
        self,
        *,
        response: Response,
        expected_status_code: Iterable[int],
        msg: str | None = None,
    ):
        assert_in(
          value=response.status_code,
          collection=expected_status_code,
          msg=(
              f'{msg or self.ERROR_MSG}\n'
              f'Код ответа: {response.status_code}\n'
              f'Текст ответа: {response.text}'
          ),
        )

    def assert_status_code_is_bad(
        self,
        response: Response,
        *,
        msg: str | None = None,
    ):
        self.assert_status_code_is_expected(
            response=response,
            expected_status_code=range(400, 404),
            msg=msg,
        )


class BaseController(AdapterMixin):
    def __init__(self, service: ImpulseedAPI) -> None:
        self.__service = service

    @property
    def service(self) -> ImpulseedAPI:
        return self.__service

from typing import Any, Iterable


def fail(msg: str | None = None) -> None:
    raise AssertionError(msg or 'Assertion failure')


def assert_in(
    *,
    value: Any,
    collection: Iterable[Any],
    msg: str = '',
) -> None:
    error_msg = f'значение: {value} не содержится в коллекции: {collection}.\n{msg}'
    if value not in collection:
        fail(error_msg)


def assert_true(
    *,
    expected: Any,
    actual: Any,
    msg: str = '',
) -> None:
    error_msg = f'ожидалось: {expected}, получено: {actual}.\n{msg}'
    if expected != actual:
        fail(error_msg)

from impulseed_autotests.controllers.content.dataclasses import Option
from impulseed_autotests.utils import get_manager_data_by_name


def check_manager_exist_in_manager_list(
    *,
    manager_name: str,
    manager_list: list[Option],
) -> None:
    assert get_manager_data_by_name(
        name=manager_name,
        manager_list=manager_list,
    )

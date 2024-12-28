from impulseed_autotests.controllers.content.dataclasses import (
    RootModel,
    BestSelectCardData,
    Option,
)


def get_manager_list(content: RootModel):
    for card_content in content.content.content:
        if (
            isinstance(card_content.data, BestSelectCardData)
            and card_content.data.name == "managers"
        ):
            return card_content.data.options


def get_manager_data_by_value(value: int, manager_list: list[Option]) -> Option:
    for manager in manager_list:
        if manager.value == str(value):
            return manager
    raise ManagerNotFoundError(str(value))


class ManagerNotFoundError(Exception):
    """Исключение для случаев, когда менеджер не найден."""
    def __init__(self, name: str):
        super().__init__(f"Менеджер с именем '{name}' не найден в списке.")


def get_manager_data_by_name(name: str, manager_list: list[Option]) -> Option:
    for manager in manager_list:
        if manager.label == name:
            return manager
    raise ManagerNotFoundError(name)


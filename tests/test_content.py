import allure

from impulseed_autotests.adapter import ImpulseedAPIAdapter
from impulseed_autotests.checkers import check_manager_exist_in_manager_list
from impulseed_autotests.utils import get_manager_data_by_value, get_manager_list


class TestContent:

    class TestChooseManage:

        @allure.title('Проверка наличия менеджера в списке')
        def test_manager_exists_in_manager_list(
            self,
            impulseed_api_adapter: ImpulseedAPIAdapter,
        ) -> None:
            with allure.step("Открытие виджета"):
                response = impulseed_api_adapter.content.api__content__get()
            with allure.step("Проверка наличия менеджера в списке"):
                check_manager_exist_in_manager_list(
                    manager_name="Матюхин Александр",
                    manager_list=get_manager_list(content=response),
                )

    @allure.title('Health check')
    def test_open_content(
        self,
        impulseed_api_adapter: ImpulseedAPIAdapter,
    ) -> None:
        impulseed_api_adapter.content.api__content__get()

    @allure.title('Получение записей менеджера')
    def test_get_manager_records(
        self,
        impulseed_api_adapter: ImpulseedAPIAdapter,
    ) -> None:
        impulseed_api_adapter.content.api__content__get(
            managers=5869968,
            start_dt=1733011200,
            end_dt=1735344000,
        )

    @allure.title('Получение записей менеджера с процентом ниже заданного по этапу 1')
    def test_get_filtered_by_first_stage_percent_records_lt(
        self,
        impulseed_api_adapter: ImpulseedAPIAdapter,
    ) -> None:
        impulseed_api_adapter.content.api__content__get(
            managers=5869968,
            start_dt=1733011200,
            end_dt=1735344000,
            stage=0,
            stage_percent=10.0,
        )

    @allure.title('Получение записей менеджера с процентом выше заданного по этапу 1')
    def test_get_filtered_by_first_stage_percent_records_gt(
        self,
        impulseed_api_adapter: ImpulseedAPIAdapter,
    ) -> None:
        impulseed_api_adapter.content.api__content__get(
            managers=5869968,
            start_dt=1733011200,
            end_dt=1735344000,
            stage=0,
            stage_percent=40.0,
        )

    @allure.title('Получение записей менеджера с процентом ниже заданного по этапу 2')
    def test_get_filtered_by_second_stage_percent_records_lt(
        self,
        impulseed_api_adapter: ImpulseedAPIAdapter,
    ) -> None:
        impulseed_api_adapter.content.api__content__get(
            managers=5869968,
            start_dt=1733011200,
            end_dt=1735344000,
            stage=1,
            stage_percent=10.0,
        )

    @allure.title('Получение записей менеджера с процентом выше заданного по этапу 2')
    def test_get_filtered_by_second_stage_percent_records_gt(
        self,
        impulseed_api_adapter: ImpulseedAPIAdapter,
    ) -> None:
        impulseed_api_adapter.content.api__content__get(
            managers=5869968,
            start_dt=1733011200,
            end_dt=1735344000,
            stage=1,
            stage_percent=40.0,
        )

    @allure.title('Получение записей менеджера с процентом ниже заданного по этапу 3')
    def test_get_filtered_by_third_stage_percent_records_lt(
        self,
        impulseed_api_adapter: ImpulseedAPIAdapter,
    ) -> None:
        impulseed_api_adapter.content.api__content__get(
            managers=5869968,
            start_dt=1733011200,
            end_dt=1735344000,
            stage=2,
            stage_percent=10.0,
        )

    @allure.title('Получение записей менеджера с процентом выше заданного по этапу 3')
    def test_get_filtered_by_third_stage_percent_records_gt(
        self,
        impulseed_api_adapter: ImpulseedAPIAdapter,
    ) -> None:
        impulseed_api_adapter.content.api__content__get(
            managers=5869968,
            start_dt=1733011200,
            end_dt=1735344000,
            stage=2,
            stage_percent=40.0,
        )

    @allure.title('Получение записей менеджера с процентом ниже заданного по этапу 4')
    def test_get_filtered_by_fourth_stage_percent_records_lt(
        self,
        impulseed_api_adapter: ImpulseedAPIAdapter,
    ) -> None:
        impulseed_api_adapter.content.api__content__get(
            managers=5869968,
            start_dt=1733011200,
            end_dt=1735344000,
            stage=3,
            stage_percent=10.0,
        )

    @allure.title('Получение записей менеджера с процентом выше заданного по этапу 4')
    def test_get_filtered_by_fourth_stage_percent_records_gt(
        self,
        impulseed_api_adapter: ImpulseedAPIAdapter,
    ) -> None:
        impulseed_api_adapter.content.api__content__get(
            managers=5869968,
            start_dt=1733011200,
            end_dt=1735344000,
            stage=3,
            stage_percent=100.0,
        )

    @allure.title('Получение записей менеджера с процентом ниже заданного по этапу 5')
    def test_get_filtered_by_fifth_stage_percent_records_lt(
        self,
        impulseed_api_adapter: ImpulseedAPIAdapter,
    ) -> None:
        impulseed_api_adapter.content.api__content__get(
            managers=5869968,
            start_dt=1733011200,
            end_dt=1735344000,
            stage=4,
            stage_percent=10.0,
        )

    @allure.title('Получение записей менеджера с процентом выше заданного по этапу 5')
    def test_get_filtered_by_fifth_stage_percent_records_gt(
        self,
        impulseed_api_adapter: ImpulseedAPIAdapter,
    ) -> None:
        impulseed_api_adapter.content.api__content__get(
            managers=5869968,
            start_dt=1733011200,
            end_dt=1735344000,
            stage=4,
            stage_percent=40.0,
        )

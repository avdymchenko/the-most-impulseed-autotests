from typing import Any

import allure
from pydantic import ValidationError

from .dataclasses import RootModel
from ...controllers import BaseController


class ContentController(BaseController):
    def api__content__get(
        self,
        *,
        managers: int | list[int] | None = None,
        stage: int | None = None,
        stage_percent: float | None = None,
        start_dt: int | None = None,
        end_dt: int | None = None,
        success: bool = True,
    ) -> RootModel | dict[str, Any]:
        with allure.step('Выполнение GET-запроса контента'):
            if isinstance(managers, int):
                managers_param = str(managers)
            elif isinstance(managers, list):
                managers_param = ",".join(map(str, managers))
            else:
                managers_param = None

            response = self.service.api_content__get(
                params={
                    'managers': managers_param,
                    'stage': stage if stage else None,
                    'stage_percent': stage_percent if stage_percent else None,
                    'start_dt': start_dt if start_dt else None,
                    'end_dt': end_dt if end_dt else None,
                },
            )
        if success:
            self.assert_status_code_is_ok(response)
            return RootModel(**response.json())
        self.assert_status_code_is_bad(response)

        return response.json()

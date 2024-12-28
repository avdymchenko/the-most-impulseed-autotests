from typing import Any

import allure
import requests
import json


class ImpulseedAPI:
    def __init__(self, *, host: str) -> None:
        self.host = host

    def api_content__get(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> requests.Response:
        url = f"{self.host}/api/content/"
        headers = {}
        query_params = params if params else None
        response = requests.get(
            url=url,
            headers=headers,
            params=query_params,
        )
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=False),
            name='Тело ответа',
            attachment_type=allure.attachment_type.JSON,
        )
        return response

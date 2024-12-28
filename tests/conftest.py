import pytest

from impulseed_autotests.fixtures import impulseed_api_adapter
from impulseed_autotests.modules.requests.utils import wrap_requests


@pytest.fixture(autouse=True, scope='session')
def wrap_rest() -> None:
    wrap_requests()

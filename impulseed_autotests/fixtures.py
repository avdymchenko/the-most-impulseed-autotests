import pytest


from impulseed_autotests.initializer import initialize_service_model
from impulseed_autotests.adapter import ImpulseedAPIAdapter
from impulseed_autotests.model import ImpulseedAPI


@pytest.fixture(scope='function')
def impulseed_api_model() -> ImpulseedAPI:
    return initialize_service_model()


@pytest.fixture(scope='function')
def impulseed_api_adapter() -> ImpulseedAPIAdapter:
    return ImpulseedAPIAdapter(initialize_service_model())

from impulseed_autotests.vars.envars import SERVICE_ENDPOINT
from impulseed_autotests.model import ImpulseedAPI


def initialize_service_model() -> ImpulseedAPI:
    service_model = ImpulseedAPI(host=SERVICE_ENDPOINT)

    return service_model

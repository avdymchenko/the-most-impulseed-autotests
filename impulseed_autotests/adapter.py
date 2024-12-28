from impulseed_autotests.controllers import AdapterMixin
from impulseed_autotests.controllers.content.controller import ContentController
from impulseed_autotests.model import ImpulseedAPI


class ImpulseedAPIAdapter(AdapterMixin):
    def __init__(self, service: ImpulseedAPI) -> None:
        self.__service = service
        self.__content_controller = ContentController(self.__service)

    @property
    def content(self) -> ContentController:
        return self.__content_controller

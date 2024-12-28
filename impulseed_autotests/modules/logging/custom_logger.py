import logging
import logging.handlers

from impulseed_autotests.modules.logging import DATE_FORMAT, FORMAT
from impulseed_autotests.modules.logging.filters import HostnameFilter


root_logger = logging.getLogger()
formatter = logging.Formatter(fmt=FORMAT, datefmt=DATE_FORMAT)
handler = logging.StreamHandler()
handler.addFilter(HostnameFilter())
handler.setFormatter(formatter)
root_logger.addHandler(handler)


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

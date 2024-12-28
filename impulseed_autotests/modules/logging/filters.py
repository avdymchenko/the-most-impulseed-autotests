import logging.handlers

from impulseed_autotests.vars import envars


class HostnameFilter(logging.Filter):
    HOSTNAME = envars.SERVICE_ENDPOINT

    def filter(self, record: str) -> bool:
        record.hostname = HostnameFilter.HOSTNAME
        return True

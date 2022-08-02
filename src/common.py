import uuid
from datetime import datetime

from pytz import timezone


class TimeStampHandler:

    def __init__(self):
        self.__TIMEZONE = timezone('Europe/Berlin')

    def get_current_date(self, format_date='%Y%m%d%H%M%S') -> str:
        d = datetime.now(self.__TIMEZONE)
        return d.strftime(format_date)


class RandomIdGenerator:

    @staticmethod
    def get_random_uuid() -> str:
        return str(uuid.uuid4())

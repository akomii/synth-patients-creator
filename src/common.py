# -*- coding: utf-8 -*
# @version: 1.0

#
#      Copyright (c) 2022  Alexander Kombeiz
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU Affero General Public License as
#      published by the Free Software Foundation, either version 3 of the
#      License, or (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU Affero General Public License for more details.
#
#      You should have received a copy of the GNU Affero General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#

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

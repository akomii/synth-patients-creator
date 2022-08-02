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
from datetime import datetime, timedelta
from random import randint, randrange

from dateutil import parser
from pytz import timezone


class TimeStampHandler:

    def __init__(self):
        self.__TIMEZONE = timezone('Europe/Berlin')

    def get_current_date(self, format_date='%Y%m%d%H%M%S') -> str:
        d = datetime.now(self.__TIMEZONE)
        return d.strftime(format_date)

    @staticmethod
    def get_random_date(start='20200101', end='20220101', format_date='%Y%m%d%H%M%S') -> str:
        start = parser.parse(start)
        end = parser.parse(end)
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        d = start + timedelta(seconds=random_second)
        return d.strftime(format_date)


class RandomStuffGenerator:

    def __init__(self, pat_id_start=1000, enc_id_start=1000):
        self.__PATIENT_ID = pat_id_start
        self.__ENCOUNTER_ID = enc_id_start

    @staticmethod
    def get_random_uuid() -> str:
        return str(uuid.uuid4())

    @staticmethod
    def get_random_postalcode() -> str:
        start = 10 ** 4
        end = (10 ** 5) - 1
        return str(randint(start, end))

    def get_enumerating_patient_id(self) -> str:
        pat_id = str(self.__PATIENT_ID)
        pat_id = ''.join(['P', pat_id])
        self.__PATIENT_ID += 1
        return pat_id

    def get_enumerating_encounter_id(self) -> str:
        enc_id = str(self.__ENCOUNTER_ID)
        self.__ENCOUNTER_ID += 1
        return enc_id

    @staticmethod
    def get_random_id(digits=10) -> str:
        start = 10 ** (digits - 2)
        end = (10 ** digits) - 1
        random_id = str(randint(start, end))
        random_id = random_id.zfill(digits)
        return random_id

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

import random

import lxml.etree as ET

from common import RandomStuffGenerator, TimeStampHandler
from patient_creator import XMLHandler


class CDAHeaderCreator:

    def __init__(self):
        self.__TIMESTAMP_HANDLER = TimeStampHandler()
        self.__RANDOM_GENERATOR = RandomStuffGenerator()

    def add_cda_header(self, tree: ET.ElementTree) -> ET.ElementTree:
        tree = self.__add_header_meta(tree)
        tree = self.__add_record_target(tree)
        tree = self.__add_author(tree)
        return tree

    def __add_header_meta(self, tree: ET.ElementTree) -> ET.ElementTree:
        root = tree.getroot()
        elem_id = tree.find('/id', root.nsmap)
        elem_id.attrib['extension'] = self.__RANDOM_GENERATOR.get_random_uuid()
        date_created = tree.find('/effectiveTime', root.nsmap)
        date_created.attrib['value'] = self.__TIMESTAMP_HANDLER.get_random_date(start='19600101')
        set_id = tree.find('/setId', root.nsmap)
        set_id.attrib['extension'] = self.__RANDOM_GENERATOR.get_random_uuid()
        return tree

    def __add_record_target(self, tree: ET.ElementTree) -> ET.ElementTree:
        base_path = '/recordTarget/patientRole'
        root = tree.getroot()
        patient_id = tree.find('/'.join([base_path, 'id']), root.nsmap)
        patient_id.attrib['extension'] = self.__RANDOM_GENERATOR.get_enumerating_patient_id()
        postal_code = tree.find('/'.join([base_path, 'addr', 'postalCode']), root.nsmap)
        postal_code.text = self.__RANDOM_GENERATOR.get_random_postalcode()
        birth_time = tree.find('/'.join([base_path, 'patient', 'birthTime']), root.nsmap)
        birth_time.attrib['value'] = self.__TIMESTAMP_HANDLER.get_random_date()
        name, gender_code = self.__get_random_gender_elements()
        patient_name = tree.find('/'.join([base_path, 'patient', 'name', 'given']), root.nsmap)
        patient_name.text = name
        birth_time.addprevious(gender_code)
        return tree

    @staticmethod
    def __get_random_gender_elements():
        gender = random.choices(['M', 'F', 'UN'], weights=[0.45, 0.45, 0.1])[0]
        if gender == 'UN':
            gender_code = ET.Element('administrativeGenderCode', attrib={'code':        'UN',
                                                                         'codeSystem':  '2.16.840.1.113883.5.1',
                                                                         'displayName': 'Undifferentiated'})
            patient_name = 'M'
        else:
            gender_code = ET.Element('administrativeGenderCode', attrib={'code':       gender,
                                                                         'codeSystem': '2.16.840.1.113883.5.1'})
            patient_name = 'Max' if gender == 'M' else 'Maximiliane'
        return patient_name, gender_code

    def __add_author(self, tree: ET.ElementTree) -> ET.ElementTree:
        base_path = '/author'
        root = tree.getroot()
        time = tree.find('/'.join([base_path, 'time']), root.nsmap)
        time.attrib['value'] = self.__TIMESTAMP_HANDLER.get_random_date()
        id_author = tree.find('/'.join([base_path, 'assignedAuthor', 'id']), root.nsmap)
        id_author.attrib['extension'] = self.__RANDOM_GENERATOR.get_random_id(digits=14)
        id_org = tree.find('/'.join([base_path, 'assignedAuthor', 'representedOrganization', 'id']), root.nsmap)
        id_org.attrib['extension'] = self.__RANDOM_GENERATOR.get_random_id()
        postal_code = tree.find('/'.join([base_path, 'assignedAuthor', 'representedOrganization', 'addr', 'postalCode']), root.nsmap)
        postal_code.text = self.__RANDOM_GENERATOR.get_random_postalcode()
        return tree

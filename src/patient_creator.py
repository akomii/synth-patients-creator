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

import lxml.etree as ET


class XMLHandler:
    __ENCODING: str = 'utf-8'

    def __init__(self):
        self.__PARSER = ET.XMLParser(remove_blank_text=True)

    def save_xml_tree(self, tree: ET.ElementTree, path_file: str):
        tree.write(path_file, xml_declaration=True, encoding=self.__ENCODING, pretty_print=True)

    def read_xml_file(self, path_file: str) -> ET.ElementTree:
        return ET.parse(path_file, self.__PARSER)

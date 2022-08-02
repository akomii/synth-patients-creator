import lxml.etree as ET

from common import RandomIdGenerator, TimeStampHandler


class CDAHeaderCreator:

    def __init__(self):
        self.__TIMESTAMP_HANDLER = TimeStampHandler()
        self.__RANDOM_ID_GENERATOR = RandomIdGenerator()

    def add_cda_header(self, tree: ET.ElementTree) -> ET.Element:
        tree = self.__add_header_meta(tree)
        return tree

    def __add_header_meta(self, tree: ET.ElementTree) -> ET.ElementTree:
        realm_code = ET.Element('realmCode', attrib={'code': 'DE'})
        id_type = ET.Element('typeId', attrib={'root':      '2.16.840.1.113883.1.3',
                                               'extension': 'POCD_HD000040'})
        id_template = ET.Element('templateId', attrib={'root': '1.2.276.0.76.10.1019'})
        id_doc = ET.Element('id', attrib={'root':      '1.2.276.0.76.3.1.192',
                                          'extension': self.__RANDOM_ID_GENERATOR.get_random_uuid()})
        code_doc_type = ET.Element('code', attrib={'code':           '68552-9',
                                                   'codeSystem':     '2.16.840.1.113883.6.1',
                                                   'codeSystemName': 'LOINC',
                                                   'displayName':    'Emergency medicine Note'})
        title = ET.Element('title')
        title.text = 'AKTIN CDA Testcase'
        date_created = ET.Element('effectiveTime', attrib={'value': self.__TIMESTAMP_HANDLER.get_current_date()})
        code_confidentiality = ET.Element('confidentialityCode', attrib={'code':       'N',
                                                                         'codeSystem': '2.16.840.1.113883.5.25'})
        code_language = ET.Element('languageCode', attrib={'code': 'de-DE'})
        id_set = ET.Element('setId', attrib={'root':      '1.2.276.0.76.4.17.9814184919',
                                             'extension': self.__RANDOM_ID_GENERATOR.get_random_uuid()})
        version = ET.Element('version', attrib={'value': '1'})
        tree.getroot().extend([realm_code, id_type, id_template, id_doc, code_doc_type, title, date_created, code_confidentiality, code_language, id_set, version])
        return tree

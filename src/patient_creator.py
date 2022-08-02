import lxml.etree as ET

from header_creator import CDAHeaderCreator


class XMLWriter:
    __ENCODING: str = 'utf-8'

    def save_xml_tree(self, tree: ET.ElementTree, path_file: str):
        tree.write(path_file, xml_declaration=True, encoding=self.__ENCODING, pretty_print=True)


class CDAFrameCreator:

    # TODO: fix this
    def create_cda_frame(self) -> ET.ElementTree:
        root = ET.Element('ClinicalDocument', attrib={'xmlns': 'urn:hl7-org:v3',
                                                      # 'xmlns:xsi':          'http://www.w3.org/2001/XMLSchema-instance',
                                                      # 'xmlns:sdtc':         'urn:hl7-org:sdtc',
                                                      # 'xsi:schemaLocation': 'urn:hl7-org:v3 ../schemas/CDA.xsd'
                                                      })
        root = self.__add_stylesheet_info(root)
        root = self.__add_model_info(root)
        tree = ET.ElementTree(root)
        return tree

    @staticmethod
    def __add_stylesheet_info(root: ET.Element) -> ET.Element:
        stylesheet = ET.ProcessingInstruction('xml-stylesheet', text='type="text/xsl" '
                                                                     'href="../stylesheets/CDA.xsl"')
        root.addprevious(stylesheet)
        return root

    @staticmethod
    def __add_model_info(root: ET.Element) -> ET.Element:
        model = ET.ProcessingInstruction('xml-model', text='href="../schematron-basis/aktin-basism20152b.sch" '
                                                           'type="application/xml" '
                                                           'schematypens="http://purl.oclc.org/dsdl/schematron"')
        root.addprevious(model)
        return root



frame = CDAFrameCreator()
treee = frame.create_cda_frame()

header = CDAHeaderCreator()
treee = header.add_cda_header(treee)

writer = XMLWriter()
writer.save_xml_tree(treee, 'abc')

from xml.etree import ElementTree as ET


class XmlImporter:
    @classmethod
    def importer(cls, file_path):
        if file_path.endswith(".xml"):
            tree = ET.parse(file_path)
            root = list(tree.getroot())
            data = []
            info_dict = {}
            for index in range(len(root)):
                for info in root[index]:
                    info_dict[info.tag] = info.text
                data.append(info_dict)
                info_dict = {}
            return data

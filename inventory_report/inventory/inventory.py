import csv
import json
from ..reports.complete_report import CompleteReport
from ..reports.simple_report import SimpleReport
from xml.etree import ElementTree as ET

class Inventory:
    @classmethod
    def import_data(self, file_path, report_type):
        data = ""
        with open(file_path, encoding="utf-8") as file:
            if file_path.endswith('.csv'):
                data = list( csv.DictReader(file, delimiter=",", quotechar='"'))
            elif file_path.endswith('.json'):
                data = json.loads(file.read())
            elif file_path.endswith('.xml'):
                tree = ET.parse(file_path)
                root = list(tree.getroot())
                data = []
                info_dict = {}

                for index in range(len(root)):
                    for info in root[index]:
                        info_dict[info.tag] = info.text
                    data.append(info_dict)
                    info_dict = {}

            if report_type == "simples":
                report = SimpleReport.generate(data)
                return report
            elif report_type == "completo":
                report = CompleteReport.generate(data)
                return report

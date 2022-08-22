import csv
import json
from ..reports.complete_report import CompleteReport
from ..reports.simple_report import SimpleReport
from ..importer.xml_importer import XmlImporter


class Inventory:
    def importer(file_path):
        data = ""
        with open(file_path, encoding="utf-8") as file:
            if file_path.endswith(".csv"):
                data = list(csv.DictReader(file, delimiter=",", quotechar='"'))
            if file_path.endswith(".json"):
                data = json.loads(file.read())
            if file_path.endswith(".xml"):
                data = XmlImporter.importer(file_path)

        return data

    @classmethod
    def import_data(self, file_path, report_type):
        data = self.importer(file_path)
        if report_type == "simples":
            report = SimpleReport.generate(data)
            return report
        elif report_type == "completo":
            report = CompleteReport.generate(data)
            return report

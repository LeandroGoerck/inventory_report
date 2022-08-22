from collections import Counter
from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, product_list):
        simple_report = SimpleReport.generate(product_list)

        most_common_products = Counter(
            product["nome_da_empresa"] for product in product_list
        ).most_common()

        last_part_report = ""
        for product, quantity in most_common_products:
            last_part_report += f"- {product}: {quantity}\n"

        return (
            simple_report + "\n"
            + "Produtos estocados por empresa:\n"
            + last_part_report
        )

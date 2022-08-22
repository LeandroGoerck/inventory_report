from collections import Counter
from .simple_report import SimpleReport

class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, product_list):
        simple_report = SimpleReport.generate(product_list)
        
        most_common_products = Counter(
            product["nome_da_empresa"] for product in product_list
        ).most_common()

        return (
          simple_report+"\n"+
            f"Produtos estocados por empresa:\n"
            f"- {most_common_products[0][0]}: {most_common_products[0][1]}\n"
            f"- {most_common_products[1][0]}: {most_common_products[1][1]}\n"
            f"- {most_common_products[2][0]}: {most_common_products[2][1]}\n"

        )
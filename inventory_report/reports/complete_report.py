from collections import Counter
from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, product_list):
        simple_report = SimpleReport.generate(product_list)

        # most_common_products
        mcp = Counter(
            product["nome_da_empresa"] for product in product_list
        ).most_common()

        return (
            simple_report + "\n" + f"Produtos estocados por empresa:\n"
                                   f"- {mcp[0][0]}: {mcp[0][1]}\n"
                                   f"- {mcp[1][0]}: {mcp[1][1]}\n"
                                   f"- {mcp[2][0]}: {mcp[2][1]}\n"
        )

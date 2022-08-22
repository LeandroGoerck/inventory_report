#  [
#    {
#      "id": 1,
#      "nome_do_produto": "CADEIRA",
#      "nome_da_empresa": "Forces of Nature",
#      "data_de_fabricacao": "2022-04-04",
#      "data_de_validade": "2023-02-09",
#      "numero_de_serie": "FR48",
#      "instrucoes_de_armazenamento": "Conservar em local fresco"
#    }
#  ]

# Data de fabricação mais antiga: YYYY-MM-DD
# Data de validade mais próxima: YYYY-MM-DD
# Empresa com mais produtos: NOME DA EMPRESA


from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, product_list):
        oldest_manufacturing_date = min(
            product_list, key=lambda x: x["data_de_fabricacao"]
        )["data_de_fabricacao"]

        closest_expiration_date = min(
            product_list, key=lambda x: x["data_de_validade"]
        )["data_de_validade"]

        company_with_more_products = Counter(
            product["nome_da_empresa"] for product in product_list
        ).most_common()[0][0]
        
        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )


# Data de fabricação mais antiga: YYYY-MM-DD
# Data de validade mais próxima: YYYY-MM-DD
# Empresa com mais produtos: NOME DA EMPRESA
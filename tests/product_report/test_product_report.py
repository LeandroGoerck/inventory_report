import string
from typing import Type
from inventory_report.inventory.product import Product


def test_relatorio_produto():
    relatorio_do_produto = Product(
        1,
        "Controle de Xbox",
        "Microsoft",
        "15/08/2022",
        "15/08/2023",
        "123456",
        "em local seco",
    )

    assert str(relatorio_do_produto) == (
    f"O produto Controle de Xbox"
    f" fabricado em 15/08/2022"
    f" por Microsoft"
    f" com validade até 15/08/2023"
    f" precisa ser armazenado"
    F" em local seco."
)


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
        "O produto Controle de Xbox"
        " fabricado em 15/08/2022"
        " por Microsoft"
        " com validade até 15/08/2023"
        " precisa ser armazenado"
        " em local seco."
    )

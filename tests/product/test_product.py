from inventory_report.inventory.product import Product


def test_cria_produto():
    testProduct = Product(
        1,
        "Controle de Xbox",
        "Microsoft",
        "15/08/2022",
        "15/08/2023",
        "123456",
        "Guardar em local seco",
    )

    assert testProduct.id == 1
    assert testProduct.nome_do_produto == "Controle de Xbox"
    assert testProduct.nome_da_empresa == "Microsoft"
    assert testProduct.data_de_fabricacao == "15/08/2022"
    assert testProduct.data_de_validade == "15/08/2023"
    assert testProduct.numero_de_serie == "123456"
    assert testProduct.instrucoes_de_armazenamento == "Guardar em local seco"

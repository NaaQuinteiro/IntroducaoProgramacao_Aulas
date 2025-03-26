tabela = {
    "Alface": 6.00,
    "Tomate": 11.00,
    "Batata": 9.00,
    "Chocolate": 5.00,
    "Banana": 3.50
}

print("-----Bem vindo ao Mercadinho Unasp------")
print()

valor_totalCompra = 0

while True:
    pergunta = input("Deseja adicionar um produto ao carrinho? \n").upper()

    if pergunta == "SIM":
        print()
        print(f"Esses são nossos produtos: \n{tabela}")
        produto_selecionado = input("Informe o nome do produto: ").capitalize()
        if tabela.get(produto_selecionado) is None:
            print("Produto não encontrado")
        else:
            quantidade_produto = float(input("Qual é a quantidade? "))

            valor_produto = tabela[produto_selecionado] * quantidade_produto

            valor_totalCompra += valor_produto
            continue

    else:
        print()
        print("Valor total da sua compra:", valor_totalCompra)
        print("-----------------Obrigada pela sua compra-----------------\n-----------------Volte sempre!-----------------")
        break


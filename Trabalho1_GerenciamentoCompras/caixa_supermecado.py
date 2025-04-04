#--------------Caixa de supermercado-----------------
estoque_produtos = {
    "Alface": {"preco": 6.00, "quantidade": 10},
    "Tomate": {"preco": 11.00, "quantidade": 8},
    "Batata": {"preco": 9.00, "quantidade": 15},
    "Chocolate": {"preco": 5.00, "quantidade": 20},
    "Banana": {"preco": 3.50, "quantidade": 12}
}

print("-----Bem vindo ao Mercadinho Unasp------")
print()

valor_totalCompra = 0

while True:
    pergunta = input("Deseja adicionar um produto ao carrinho? (S/N)\n").upper()

    if pergunta == "S":
        print("-------------Esses são nossos produtos--------------")
        for produto, dados in estoque_produtos.items():
            print(f"{produto} | Preço: R${dados['preco']:.2f} | Quantidade disponível: {dados['quantidade']}")
            print()
       
        produto_selecionado = input("Informe o nome do produto: ").capitalize()
        if estoque_produtos.get(produto_selecionado) is None:
            print("Produto não encontrado")
        else:
            quantidade_produto = float(input("Qual é a quantidade? "))

            valor_produto = estoque_produtos[produto_selecionado] * quantidade_produto

            valor_totalCompra += valor_produto
            continue

    else:
        print()
        print("Valor total da sua compra:", valor_totalCompra)
        print("-----------------Obrigada pela sua compra-----------------\n-----------------Volte sempre!-----------------")
        break


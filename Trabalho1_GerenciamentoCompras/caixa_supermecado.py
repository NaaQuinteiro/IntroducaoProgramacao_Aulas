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
            add_product = input("O produto selecionado não foi encontrado no estoque\nDeseja adicioná-lo? (S/N)").upper()
            
            if add_product == "S":
                product_name = input("Insira o nome do produto: ").capitalize()
                product_price = float(input("Insira o preço: "))
                quantity = int(input("Insira a quantidade do estoque: "))

                estoque_produtos[product_name] = {
                    "preco": product_price,
                    "quantidade": quantity
                }
                continue   
        else:
            quantidade_produto = float(input("Qual é a quantidade? "))

            if estoque_produtos[produto_selecionado]["quantidade"] >= quantidade_produto:

                estoque_produtos[produto_selecionado]["quantidade"] -= quantidade_produto

                valor_produto = estoque_produtos[produto_selecionado]["preco"] * quantidade_produto

                valor_totalCompra += valor_produto
                continue
            print("Sinto muito, quantidade indisponível no estoque")
        continue

    else:
        print("-----------------Obrigada pela sua compra-----------------")
        print("Valor total da sua compra:", valor_totalCompra)
        print("--------------------Volte sempre!---------------------\n")
        break


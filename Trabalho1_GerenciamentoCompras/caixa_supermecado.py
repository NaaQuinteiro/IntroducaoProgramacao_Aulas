#--------------Caixa de supermercado-----------------
import time 
product_stock = {
    "Alface": {"preco": 6.00, "quantidade": 10},
    "Tomate": {"preco": 11.00, "quantidade": 8},
    "Batata": {"preco": 9.00, "quantidade": 15},
    "Chocolate": {"preco": 5.00, "quantidade": 20},
    "Banana": {"preco": 3.50, "quantidade": 12}
}

print("-----Bem vindo ao Mercadinho Unasp------")
print()

total_purchase_value = 0

while True:
    question = input("Deseja fazer sua compra? (S/N)\n").upper()

    if question == "S":
        print("-------------Esses são nossos produtos--------------")
        for product, data in product_stock.items():
            print(f"{product} | Preço: R${data['preco']:.2f} | Quantidade disponível: {data['quantidade']}")
            print()
       
        selected_product = input("Informe o nome do produto: ").capitalize()
        if product_stock.get(selected_product) is None:
            add_product = input("O produto selecionado não foi encontrado no estoque\nDeseja adicioná-lo? (S/N)").upper()
            
            if add_product == "S":
                new_product_name = input("Insira o nome do produto: ").capitalize()
                new_product_price = float(input("Insira o preço: "))
                new_product_quantity = int(input("Insira a quantidade do estoque: "))

                product_stock[new_product_name] = {
                    "preco": new_product_price,
                    "quantidade": new_product_quantity
                }
                continue   
        else:
            product_quantity = float(input("Qual é a quantidade? "))

            if product_stock[selected_product]["quantidade"] >= product_quantity:
                product_stock[selected_product]["quantidade"] -= product_quantity

                product_value = product_stock[selected_product]["preco"] * product_quantity

                total_purchase_value += product_value
                continue
            else:
                print("Sinto muito, quantidade indisponível no estoque, por favor, selecione outro produto ou uma quantidade válida")
                time.sleep(0.5)
                print()
        continue

    else:
        print("-----------------Obrigada pela sua compra-----------------")
        print("Valor total da sua compra:", total_purchase_value)
        print("--------------------Volte sempre!---------------------\n")
        break

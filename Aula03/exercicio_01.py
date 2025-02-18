# Programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a procentagem do aumento. 
# Exiba o novo salario

# Entrada de dados
valor_salario = float(input("Insira o valor do seu salário ex: R$ 1000\nR$ "))

porcentagem_aumento = float(input("Insira a porcentagem de aumento ex: 10\n% "))

# Processamento
aumento = (valor_salario * porcentagem_aumento)/100

novo_salario = valor_salario + aumento

# Saída
print(f"Salário: R${valor_salario}\nPorcentagem: {porcentagem_aumento}\nAumento: {aumento}\nNovo Salário: R${novo_salario}")
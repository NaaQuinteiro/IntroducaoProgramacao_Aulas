# Programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e o cargo;
# Se SENIOR o aumento é de 20%, se PLENO de 15% e se JUNIOR 10%;

# Entrada de dados
valor_salario = float(input("Insira o valor do seu salário ex: R$ 1000\nR$ "))

cargo = input("Insira o cargo ocupado: ").lower()

# Processamento
if cargo == "senior" or cargo == "sênior":
    porcentagem_aumento = 20
elif cargo == "pleno":
    porcentagem_aumento = 15
elif cargo == "junior" or cargo == "júnior":
    porcentagem_aumento = 10
else:
    print("O cargo informado não possuí aumento de salário")

aumento = (valor_salario * porcentagem_aumento)/100

novo_salario = valor_salario + aumento

# Saída
print(f"Salário: R${valor_salario}\nCargo: {cargo}\nPorcentagem: {porcentagem_aumento}\nAumento: {aumento}\nNovo Salário: R${novo_salario}")

def calcular_aumento_salarial(cargo, salario):

    if cargo == "senior":
        porcentagem_aumento = 20
    elif cargo == "pleno":
        porcentagem_aumento = 15
    elif cargo == "junior":
        porcentagem_aumento = 10
    else:
        print("O cargo informado não possuí aumento de salário")
    
    aumento = (salario * porcentagem_aumento)/100

    return salario + aumento

cargo = input("Informe o seu cargo: ")
salario = float(input("Informe o seu salario: "))

print(f"O seu novo salário é de R${calcular_aumento_salarial(cargo, salario)}")
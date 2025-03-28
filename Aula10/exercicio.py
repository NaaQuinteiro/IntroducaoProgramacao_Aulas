def eh_par(x):
    if(x %2 == 0):
        return "par"
    else:
        return "impar"

numero = int(input("Insira o numero: "))

print(f"O número {numero} é {eh_par(numero)}")


lista = [4, 7, 8, 9, 10, 11, 34, 5, 8]
resultado = []

for i in lista:
    x = eh_par(i)
    resultado.append({"Número": i, "Resultado": x})
print(resultado)
print()

resultadoSimples = [(i, eh_par(i))for i in lista if i>5]
print(resultadoSimples)
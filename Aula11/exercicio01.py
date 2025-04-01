def somar_lista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma


def calcular_media(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma/len(lista)

lista = [1,2,3]

print(somar_lista(lista), calcular_media(lista))

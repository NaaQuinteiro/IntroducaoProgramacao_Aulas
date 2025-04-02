try:
    x = y + 2
except:
    print("Houve um erro")
    pass

try:
    x = y + 2

#ERRO GENÉRICO
except Exception as e:
    print("EXCEPION AS E: ", e)

try:
    x = y + 2
#ERRO DE TIPO
except TypeError as e:
    print("TYPE ERROR AS E: ", e)
#ERRO DE NOME
except NameError as e:
    print("NAME ERROR AS E: ", e)


def eh_par(x):
    try: 
        if(x %2 == 0):
            return "par"
        else:
            return "impar"
    except TypeError as e:
       return "Error de tipo"

resultado = [eh_par(i) for i in [5, 3, "a", 7, 2, "b"]]
print(resultado)

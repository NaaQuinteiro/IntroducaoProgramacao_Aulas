# # print("Hello World!")

# #--------- Variáveis --------#
# #Inteiro int
# a = 10 
# b = a + 5
# print(b)
# #N° reais, float
# c = 10.34 

# #String, str
# d = "Olá mundo" 
# print(d) 

# #Boolean, bool
# e = True
# f = False

# #Função type permite saber o tipo da variável 
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# #Bibliotecas (Importa-se no incio do código)
# import math # biblioteca python que executa operações matemáticas
# g = math.sqrt(144)
# print(g)

# # #Concatenação 
# # print("O valor da raiz quadrada de 144 = ", g)

# # print(f"O valor da raiz quadrada de 144 = {g}")

# #Entrada de dados 
# numero1 = float(input("Escreva um número: ")) #tipando o input
# numero2 = input("Escreva um número: ") # sem tipar, ele vai transformar tudo em string, portanto aceita qlqr valor

# raiz = math.sqrt(numero1) #aqui eu não poderia passar o numero 2 pq ele é string e a função não aceita strings,ele n da erro aqui mas quando o codigo é executado ele quebra, requisitando um valor do tipo numero reais
# print(raiz)

#--------------- AULA 02 --------------

number1 = float(input("Digite um numero: "))

number2 = float(input("Digite um numero: "))

number3 = float(input("Digite um numero: "))

media = (number1 + number2 + number3) / 3


print(f"A média dos numeros {number1}, {number2} e {number3}: {media}") #usa a formatação padrão

print(f"A média dos numeros {number1}, {number2} e {number3}: {media:.2f}") #formata para duas casas decimais depois da virgula



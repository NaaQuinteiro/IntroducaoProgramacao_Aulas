
# Fazer adicionar na lista apenas se i for um numero par.
y = [i**2 for i in range(0, 10) if i%2 == 0]
print(y)


#Printar o numero de espaços na palavra 
contagem = 0
for i in "eu estudo no unasp":
    if i == " ":
        contagem += 1
    
print("A frase contém:",contagem,"espaço(s)")

#Contar quantas letras tem, exceto o espaço
soma = 0
for i in "eu estudo no unasp":
    if i != " ":
        soma += 1
    
print("A frase contém:",soma,"letra(s)")

#Cria uma lista de 0 a 9
for i in range(0, 10):
    print(i)

#Como salvar cada um desses elementos da lista gerada em uma nova lsita?
newList = []

for i in range(0, 10):
    newList.append(i**2) #função que adiciona 1 elemento no final da lista

print(newList)

# list comprenhesion
y = [i**2 for i in range(0, 10)]
print(y)

# list comprenhesion também permite condições
y = [i**2 for i in range(0, 10) if i < 5]
print(y)
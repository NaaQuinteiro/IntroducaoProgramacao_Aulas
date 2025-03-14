x = [1, 2, 3, 4.5, "maria", True, False]
print(x[0])#printa o primeiro item da lista
print(x[-1]) #printa o ultimo item da lista
print(x[-2]) #printa o penultimo item da lista
print(x[3:5]) #printa o que está na posição 3° e 4° posição, o 5 é o limite, por isso n printa true
print(x[3:]) #printa do indice 3 até o final

#Substituindo valores nas posições 
x[2] = "Valor do 2° index foi substituido por essa frase"
print(x)

# Extraindo valores de listas encadeadas 

#  ----0-------1-----
y = [[1, 2], [3, 4]]
# ----0--1----0--1------

print(y[1][0]) #printe o que está na segunda lista (pq ela ta no indice 1) no idice 0
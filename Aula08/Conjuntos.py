# Set, um conjunto que nao permite que nada seja repitido, então ele deleta, e ordena as coisas
A = {1, 2, 3, 3, 4, 4}
print(A)

#Também podemos fazer operações de conjuntos entre eles, então vamos fazer outro SET
B = {1, 2, 3, 4}
C = {2, 4, 8, 9}

#Intersecção (Compara o que se tem de igual entre os conjuntos e apresenta)
x = B & C
print(x)
#União (Tras a união de entre os conjuntos)
y = B | C
print(y)

#Diferença entre os conjunto, mostra o que tem em um mas n tem no outro
z = B - C
print(z)
w = C - B
print(w)

# Diferença simétrica, tras a união das diferenças entre os conjuntos 
v = B ^ C
print(v)

# Pertence, verifica se determinada coisa pertence ou não a algo e retrona um boolean
d = 4 in (A)
print(d)
notD = 4 not in (A)
print(d, notD)

#Podemos transformar sets em listas, listas em tuplas e vice versa 
e = tuple(set(list(A)))
print(e, "Virei uma tupla!")
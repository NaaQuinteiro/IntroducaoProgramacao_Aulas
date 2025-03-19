# São declaradas por parenteses, e são imutáveis, não pode-se substituir valores, diferente da lista 
x = (1, 2, 3, True, "maria")

# As tuplas são interessantes para criação de registros de informações que não serão modificadas, preservando a ordem das informações
#ex: quero salvar o nome, a idade e se tem filho ou não 
registro = ("maria", 30, True)

# Podemos fazer como se fosse um banco de dados, salvando tuplas em listas
listaDeTuplas = [("maria", 30, True), ("joao", 40, False) ]
tuplaDeTuplas = (("maria", 30, True), ("joao", 40, False))

#também podemos percorrer as tuplas
for i in tuplaDeTuplas:
    print(i) # -- printa as tuplas 

# Como printar o nome dentro da tupla de tupla
for i in tuplaDeTuplas:
    print(i[0]) # -- printa um item especifico dentro da tupla


for i in listaDeTuplas:
    print(i[2]) # -- printa um item especifico dentro da tupla dentro da lista

# Adição de dados no final da tupla é permitido!!!
df = (("maria", 30, True), ("joao", 40, False))
df = df + (("marcos", 50, True),) #-- adiciona o elemento dentro da tupla (Faz uma concatenação)
print(df)
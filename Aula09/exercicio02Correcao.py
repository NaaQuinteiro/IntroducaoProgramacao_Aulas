# Criar um dicionário que armazena nas chaves todas as letras de uma frase e no valor de cada uma a quantidade delas na frase

letras = {}

# Loop para percorrer a frase 
for i in "eu estudo no unasp":
    if i != " ":
        # Adiciona no dicionario em i, a chave com o valor de i e o valor inicial de 0 e depois + 1
        letras[i] = letras.get(i, 0) + 1
# Saída 
print(letras)
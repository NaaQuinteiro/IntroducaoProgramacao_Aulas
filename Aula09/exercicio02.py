# Criar um dicionário que armazena nas chaves todas as letras de uma frase e no valor de cada uma a quantidade delas na frase

letras_frase = {}

frase = "amo amar"

# Retirar os epaços da frase 
frase = frase.replace(" ", "")

# Loop para percorrer a frase 
for i in frase:
    # Adiciona no dicionario em i, a chave com o valor de i e o valor inicial de 0 e depois + 1
    letras_frase[i] = letras_frase.get(i, 0) + 1

# Saída 
print(letras_frase)
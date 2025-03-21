# Dicionários são conjuntos de chave e valor
dicionario = {"key": "value", "chave": "valor", "y": [True, False], "numro": 1}

#Exgtrair valor do dicionário passamos da mesma forma que fazemos em lista mas ao inves do index podemos passar a cheve 
# ela vai nos retornar o conteudo da chave: 
print(dicionario["numro"])
print(dicionario["chave"])
print(dicionario["y"][1])

# Podemos usar o get também para retornar o valor de determinada chave
print(dicionario.get("key")) #---- me tras o valor vinvulado a chave key

# Quando o get não encontra determinada chave ele printa None a invés de der erro;
# Portanto se depois da cheve colocarmos virgula e um valor, ele retorna esse valor quando a chave n é encontrada
print(dicionario.get("numero", "Chave não encontrada!"))


# Adicionando dados no dicionário, passamos o dicionario[chave que tera] = valor 
dicionario["Adiciona chave"] = "Nova chave"

print(dicionario)
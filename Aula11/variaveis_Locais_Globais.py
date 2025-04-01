a = "variavel global"

def funcao():
    #dizer que uma variavel é global
    global a
    a = "variavel local"
    return a

print(funcao())
print(a)

# Colocar o global + variavel, faz o progrma entender que o a dentro da função passara a ser global
# portanto as alterações dentro da função deixam de ser locais. 


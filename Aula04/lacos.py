i = 1

while i <= 10:
    print(i)
    i += 1


while True:
    print("Estou em um loop")
    
    sair = input("Quer sair?")    
    if sair == "Sim":
        print("Bye")
        break
    else:
        continue
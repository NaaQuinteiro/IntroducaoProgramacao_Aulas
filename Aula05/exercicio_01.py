#Tabuada 

while True:
    i = 0

    tabuada = int(input("Insira o número que deseja calcular a tabuada: "))
    
    while i < 10:
        print(f"{tabuada} x {i} = {tabuada * i}"  )
        i += 1
    
    escolha = int(input("\nDeseja continuar? \n 1 - Sim \n 2 - Não\n "))
    
    if escolha != 1:
        print("\nVocê está saindo do programa...Tchau!")
        break
    else:
        continue

   
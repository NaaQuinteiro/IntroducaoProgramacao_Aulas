import os #Biblioteca de interação com o sistema operacional
import time #Biblioteca de tempo

i = 1

size, _ = os.get_terminal_size()

while i <= size:
    progresso = 100 * i/size #calcular a porcentagem de progresso 

    print(f"{chr(9608) * i} {progresso:.0f}%")
    time.sleep(0.1) #espera 3 Milessegundo para limapr
    os.system("cls")
    i += 1

    
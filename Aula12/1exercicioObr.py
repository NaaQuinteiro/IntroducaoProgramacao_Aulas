i = 0
vitoria = 0
while i <= 6:
   i += 1
   x= input("Insira: ")
   if x == "V":
     vitoria += 1
    

if vitoria >= 5:
    print(1)
elif (vitoria == 3) or (vitoria == 4):
    print(2)
elif (vitoria == 1) or (vitoria == 2):
    print(3)
else:
    print(-1)
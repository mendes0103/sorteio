import os
os.system("cls")
import random
print ("lista aleatoria")
n=1
while True: 
   obj1= 'pirulito'
   obj2= 'bala'
   obj3= 'paçoca'
   obj4= 'chiclete'
   lista= [obj1, obj2, obj3, obj4]
   escolhido= random.choice(lista)
   print (f"parabéns, voce ganhou: {escolhido} ")
   r1= str(input("deseja fazer outro sorteio?"))
   if r1 != "sim":
        print ("okay, ate a proxima!")
        break


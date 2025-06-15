import random 

maquina= random.randint (0,5)



usuario=int(input("digite um numero de 0 a 5:"))

if maquina == usuario:
    print('correto!')


else:
    print ("errado!!")


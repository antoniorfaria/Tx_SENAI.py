velocidade = int(input("Velocidade do carro em KM/H:"))
multa=80 


if velocidade > multa:
    valorApagar= (int(velocidade - multa)*7)
    print (f"valor final é igual a R$: {valorApagar}")

else:
    print (f'não foi multado')

    
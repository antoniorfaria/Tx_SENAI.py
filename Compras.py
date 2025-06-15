# valor gasto por um usuario 

# metodo de pagamento 
# Dinheiro/Pix = 10% Desconto
# Credito = normal

valorGasto = int(input("digite o valor gasto: "))
print("Método de pagamento:" )
print("1 - Dinheiro/Pix: ")
print("2 - credito: ")

metodoPagamento = input("digite o metodo de pagamento")

if metodoPagamento ==  "1":
    valorFinal = valorGasto * 0.3
    print (f"Valor fnal é igual o {valorFinal}")


else:
 print(f"valor final é igual a R$: {valorGasto}")
    

valorGasto = int(input("digite o valor gasto: "))
print("Método de pagamento:" )
print("1 - Dinheiro/Pix: ")
print("2 - credito: ")
print("3 - Débito: ")

metodoPagamento = input("digite o metodo de pagamento: ")

if metodoPagamento ==  "1":
    valorFinal = valorGasto * 0.3
    print (f"Valor fnal é igual R$ {valorFinal}")

elif metodoPagamento == "3":
    
    valorFinal = valorGasto *0.95
    
    print (f"Valor fnal é igual R$ {valorFinal}")
    
    

else:
   
    print ("1 - A vista")
    print ("2 - 2x")      
    print ("3 - 3x")

    metodosDeparcelamento= (input("digite quanto deseja parcelar:" ))
        
    if metodosDeparcelamento == "2":
        
            valorFinal = valorGasto*1.05
            
            print (f"Valor fnal é igual R$ {valorFinal}")
    
            
    elif metodosDeparcelamento == "3" :
        
            valorFinal= valorGasto*1.1
            
            print (f"Valor fnal é igual R$ {valorFinal}")
    
            
    else:
      print (f"Valor final é igual R$ {valorGasto}")
         
     
        
    

    
    
 

    
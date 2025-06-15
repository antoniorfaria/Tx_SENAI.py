listaTimes = ["Corinthians Grande" , "Palmares" , "SantosB" , "chupaulo"]

#Adicionar itensbem uma lista ( vai sempre para o ultimo lugar)

listaTimes.append ("Chelsea")
listaTimes.append ("mundial")

print (listaTimes) 


#Adicionando item numa posição especifica

listaTimes.insert (1 , "VArmengo")
print (listaTimes)

#verificando o  tamanho de uma lista

print (len(listaTimes))

#Remover um item da lista

listaTimes.remove( "Palmares")

print (listaTimes)

#Pegando a posiçãode item na lista


print (listaTimes.index ("Corinthians Grande"))


#Organizando lista em ordem alfabetica

print(sorted(listaTimes))


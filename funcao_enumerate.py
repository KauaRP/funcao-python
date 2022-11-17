# funcaço enumerate enumera indice de estrutura de dados 
 
 #retornar o indice de uma lista

animais = ["cachorro","gato","periquito","elefante"]

print(list(enumerate(animais)))

 ## iterar com enumerate

for i,valor in enumerate (animais):
    print (i,valor)


    ## iterador e enumerate com condicionais

for i,valor in enumerate(animais):
        if i>1:
            break
        else:
            print(valor)


 
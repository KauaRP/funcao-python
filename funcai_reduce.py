### função reduce
# serve para reduzir os valores de uma estrutura de dados
# a um unico valor

# precisamos importar um modulo builtin chamado functools

from functools import reduce

lista = [2,7,10,6,78]

def mult(x,y):
    return x*y

print(reduce(mult,lista))

## testar o maior valor usando a reduce

lista2 = [30,67,1000,61,90]

testmaior + lamba x,y: x if (x>y) else y

print (reduce(testmaior,lista2))
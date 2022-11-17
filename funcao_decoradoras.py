# funções decoradores servem para potencializar (dar mais recursos) para outras
#funcões.
# para utilizar uma função decorada utilizar o @ antes do nome da função
# e acima da função que sera decorada(receberá os podores da outra função)


## criar a função decoradora

def master(msg):
    def imprime():
        print("essa é a função Decorada")
        msg()
        return imprime



# Segunda função que vai ser utilizada junto com a decoradora

@master
def funcao_simples():
    print("Estou chamando a função simples")


funcao_simples()

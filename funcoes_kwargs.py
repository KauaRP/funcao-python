## funções kwargs
# passar um numero indeterminado de parametros
# para função. Mas diferente do arg voce precisa
# passar nos argumentos indetificador de chaves e valores

def saudacoes (**kwargs):
    print (kwargs)

    saudacoes(manha="bom dai",tarde="bom tarde")

def saudacao_dia (**kwargs):
    for periodo_dia,saudacao in kwargs.item():
        print(f"durante a {periodo_dia}dizemos{saudacao}") #fstrings

## chamar a função

saudacao_dia(manha="bom dia", tarde+"boa tarde",noite="boa noite",madrugada="vai dormiii")

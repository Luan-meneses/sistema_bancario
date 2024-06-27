def somador(valor_1, valor_2):
    return valor_1 + valor_2
c = 0
while c < 5:
    valor_1 = int(input('VALOR: '))
    valor_2 = int(input('VALOR: '))

    resposta = somador(valor_1, valor_2)
    print("resposta", resposta,   c)
    c = c + 1
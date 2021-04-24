v = (int(input('Qual foi a distância da viagem? ')))
if v < 200:
    v = v * 0.5
    print('O valor da viagem ficou em: {:.2f}R$'.format(v))
else:
    v = v * 0.45
    print('O valor da viagem ficou em: {:.2f}R$'.format(v))

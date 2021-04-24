d = (int(input('Quantos dias o carro ficou alugado? ')))
km = (float(input('Quantos kilômetros o carro "rodou"? ')))
p = (d * 60) + (km * 0.15)
print('O valor total do aluguel do carro foi de R${:.2f}'.format(p))

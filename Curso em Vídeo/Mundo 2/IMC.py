p = float(input('Digite aqui o peso(em Kg):  '))
a = float(input('Digite aqui a altura(em m): '))
IMC = p / (a ** 2)
print('O IMC calculado foi de: {:.2f}'.format(IMC))
if IMC > 40:
    print('Cuidado, o IMC calculado está na faixa de obesidade mórbida.')
elif IMC >= 30:
    print('O IMC calculado está na faixa de obesidade.')
elif IMC >= 25:
    print('O IMC calculado está na faixa de sobrepeso.')
elif IMC >= 18.5:
    print('O IMC calculado está na faixa de peso ideal.')
else:
    print('O IMC calculado está na faixa de abaixo do peso ideal.')

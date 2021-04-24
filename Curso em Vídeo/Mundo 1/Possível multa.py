v = float(input('Qual era a verlocidade do carro?(em Km/h) '))
if v > 80:
    print('O condutor foi multado por excesso de velocidade ao estar à {:.1f}Km/h.'.format(v))
    m = (v - 80) * 7
    print('O condutor deverá pagar uma multa de {:.2f}R$'.format(m))
else:
    print('O condutor não foi multado.')

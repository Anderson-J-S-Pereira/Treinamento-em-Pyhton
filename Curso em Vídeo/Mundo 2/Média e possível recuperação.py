n1 = float(input('Qual o primeiro valor da média? '))
n2 = float(input('Qual o segundo valor da média? '))

med = (n1 + n2) / 2
print('A média é de {} pontos.'.format(med))

if med >= 7:
    print('Parabéns está aprovado!')
elif med >= 5:
    print('Estará de recuperação.')
elif med < 5:
    print('Sinto muito, mas foi reprovado.')

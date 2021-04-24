i = int(input('Quantos anos completos tem? '))
if i > 18:
    ft = i - 18
    print('Já passou da hora de fazer o alistamento militar.')
    print('Fazem {} ano(s) que deveria ter se alistado.'.format(ft))
elif i == 18:
    print('Está na época de fazer o alistamento.')
else:
    ft_1 = 18 - i
    print('Não está no momento de alistamento... ainda...')
    print('Deverá se alistar daqui há {} ano(s).'.format(ft_1))

i = int(input('Quantos anos completos tem? '))

if i <= 9:
    print('Classificação: Mirim.')
elif i <= 14:
    print('Classificação: Infantil.')
elif i <= 19:
    print('Classificação: Júnior.')
elif i == 20:
    print('Classificação: Sênior.')
else:
    print('Classificação: Master.')

from random import randint

comp = randint(1, 10)
palpite = 1
print('Pensei em um número de 0 à 10, tente adivinhar.')
chute = int(input('Qual número irá chutar? '))

while comp != chute:
    if comp > chute:
        print('É mais, continue tentando.')
    elif chute > comp:
        print('É menos, continue tentando.')
    palpite += 1
    chute = int(input('Qual número irá chutar? '))

print('Parabéns, realmente era {}.'.format(comp))

if palpite < 1:
    print('Conseguiu com {} tentativa.'.format(palpite))
else:
    print('Conseguiu com {} tentativas.'.format(palpite))

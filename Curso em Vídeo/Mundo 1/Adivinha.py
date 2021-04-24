import random
n = int(random.randint(1, 5))
a = int(input('Tente adivinhar: Qual número de 1 à 5 eu pensei? '))
if n == a:
    print('Caramba! Adivinhou, realmente era {}.'.format(n))
else:
    print('Que pena! Você escreveu {}, mas era {}.'.format(a, n))

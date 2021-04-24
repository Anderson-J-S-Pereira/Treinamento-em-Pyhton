n = int(input('Digite um número inteiro para saber se é ímpar ou par: '))
n_1 = n % 2
if n_1 == 0:
    print('O número digitado({}) é par.'.format(n))
else:
    print('O número digitado ({}) é ímpar.'.format(n))

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
    print('O primeiro valor: {} é maior que {}.'.format(n1, n2))
elif n1 == n2:
    print('Ambos tem o mesmo valor. {} é igual a {}.'.format(n1, n2))
else:
    print('O segundo valor: {} é maior que {}.'.format(n2, n1))

num = int(input('Digite o número a ser verificado: '))
cont = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m{} é divisível por {} número(s).'.format(num, cont), end=' ')
if cont > 2:
    print('Portando NÃO é primo.')
else:
    print('Portanto É primo.')

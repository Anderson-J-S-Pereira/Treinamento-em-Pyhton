n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão: )
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal''')
e = int(input('Escolha sua opção: '))
if e == 1:
    print('O valor {} convertido em binário é: {}.'.format(n, bin(n)))
elif e == 2:
    print('O valor {} convertido em octal é: {}.'.format(n, oct(n)))
elif e == 3:
    print('O valor {} convertido em hexadecimal é: {}.'.format(n, hex(n)))
else:
    print('Número inválido, tente novamente.')

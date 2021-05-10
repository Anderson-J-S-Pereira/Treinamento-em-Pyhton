from time import sleep
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
r = 0
op = 0
print('Os valores inseridos foram {} e {}.'.format(n1, n2))
while op != 3:
    op = int(input('''Digite os seguintes valores para as operações requeridas:
    1. Soma
    2. Maior
    3. Sair do programa
    '''))
    if op == 1:
        r = n1 + n2
        print('O resultado da soma é {}.'.format(r))
    elif op == 2:
        if n1 > n2:
            r = n1
            print('O maior valor é {}.'.format(r))
        elif n2 > n1:
            r = n2
            print('O maior valor é {}.'.format(r))
        elif n1 == n2:
            print('Os valores são iguais.')
print('Finalizando...')
sleep(1)
print('Finalizado.')
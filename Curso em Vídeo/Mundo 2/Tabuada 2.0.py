n = int(input('Digite um valor para ser calculada sua tabuada: '))
f = int(input('Até qual valor deseja calcular? '))
cont = 0
r = 0
for c in range(1, f+1):
    cont = cont + 1
    r = n * cont
    print('{} x {} é: {}.'.format(n, cont, r))

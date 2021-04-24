pt = int(input('Qual o primeiro número da razão da Progressão Aritmética? '))
ra = int(input('Qual a razão dela? '))
de = pt + (10 - 1) * ra
for c in range(pt, de, ra):
    print('{} '.format(c), end= ' -> ')
print('Fim.')

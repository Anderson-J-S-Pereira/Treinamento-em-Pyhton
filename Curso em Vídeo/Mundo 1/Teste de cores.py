teste = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'} # Acredito que isso seja um tipo de biblioteca

print('{}Testando {}cores {}de outra maneira{}.'.format(teste['azul'], teste['amarelo'], teste['pretoebranco'], teste['limpa']))

print('\033[0;35;47mOlá mundo!')
print('\033[7;37;40mOlá mundo!')
print('\033[5;36;47mOlá mundo!')
print('\033[mOlá mundo!') # Sem cores

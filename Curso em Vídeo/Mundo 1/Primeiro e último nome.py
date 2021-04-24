n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em lhe conhecer!')
print('Seu primeiro nome é: {}'.format(nome[0]))
# Essa foi a tentativa
print('Seu último nome é: {}'.format(nome[len(nome)-1]))

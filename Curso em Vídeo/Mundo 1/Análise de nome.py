nome = str(input('Digite seu nome completo: ')).strip()
# Letras maiúsculas
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
# Letras minúsculas
print('Seu nome em minúsculas {}: '.format(nome.lower()))
# Contagem de letras (idealmente sem os espaços)
print('Seu nome completo tem {} letras.'.format(len(nome) - nome.count(' ')))
# Quantas letras tem o primeiro nome
div = (nome.split())
p = div[0]
print('Seu primeiro nome é {} e ele tem {} letras.'.format(div[0], len(p)))

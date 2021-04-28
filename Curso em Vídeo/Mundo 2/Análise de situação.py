# ------ Variáveis ------
soma_idade = 0
hv = 0
iv = 0
im = 0

# ------ Programa ------
quant = int(input('Quantas pessoas deseja analisar? '))
for pessoas in range (1, quant + 1):
    print('----- {}° pessoa -----'.format(pessoas))
    nome = str(input('Qual o nome? ')).strip()
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual o sexo? [M/F]? ')).strip()
    soma_idade += idade
    if sexo == 'F' or sexo == 'f' and idade < 20:
        im += 1
    if sexo in 'Mm' and idade > iv:
        iv = idade
        hv = nome

media_idade = soma_idade / pessoas

# ------ Saída ------
print('A média da idade das pessoas requeridas é de {:.0f} anos.'.format(media_idade))
print('{} é o homem mais velho com {} anos.'.format(hv, iv))

if im == 0:
    print('Não há mulheres com menos de 20 anos.')
elif im == 1:
    print('Há {} mulher com menos de 20 anos.'.format(im))
else:
    print('Existem {} mulheres com menos de 20 anos.'.format(im))

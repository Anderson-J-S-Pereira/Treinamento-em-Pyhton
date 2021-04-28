# ------ Importações ------
from datetime import date
# ------ Contadores ------
t_maior = 0
t_menor = 0
# ------ Programa ------
quant = int(input('Quantas pessoas deseja avaliar? '))
for pessoas in range (1, quant+1):
    ano_nasc = int(input('Qual foi o ano de nascimento da {}° pessoa? '.format(pessoas)))
    idade = date.today().year - ano_nasc
    print('A pessoa tem atualmente em {} a idade de {} anos.'.format(date.today(), idade))
    if idade >= 18:
        print('A pessoa JÁ alcançou a maioridade.')
        t_maior += 1
    else:
        print('A pessoa NÃO alcançou a maioridade.')
        t_menor += 1
print('Ao todo temos nesse grupo {} pessoas que JÁ alcançaram a maioridade.'.format(t_maior))
print('E temos ao todo {} pessoas que NÃO alcançaram a maioridade'.format(t_menor))

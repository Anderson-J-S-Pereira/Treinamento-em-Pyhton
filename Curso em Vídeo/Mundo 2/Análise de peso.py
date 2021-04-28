# ------ Variáveis
quant_p = int(input('Quantas pessoas deseja analisar? '))
pm = 0
pme = 0

# ------ Programa ------
for pessoas in range (1, quant_p + 1):
    peso = float(input('Qual o peso da {}° pessoa? '.format(pessoas)))

    if pessoas == 1:
        pm = peso
        pme = peso

    if peso >= pm:
        pm = peso

    if peso <= pme:
        pme = peso

# ------ Saída ------
print('A pessoa de maior peso tem {} Kg.'.format(pm))
print('A pessoa de menor peso tem {} Kg.'.format(pme))

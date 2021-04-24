sal = float(input('Qual o salário atual? '))
por = float(input('O salário aumentará em quantos porcento? '))
aum = sal + ((sal / 100) * por)
print('O novo salário será de R${:.2f}'.format(aum))
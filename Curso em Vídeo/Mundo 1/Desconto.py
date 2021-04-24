v = float(input('Qual o valor do produto? '))
d = float(input('Quantos porcento de desconto o produto receberá? '))
v1 = (v / 100) * (100 - d)
print('O novo valor do produto será de R${:.2f}'.format(v1))
v2 = v - v1
print('O produto teve um desconto equivalente a R${:.2f}'.format(v2))


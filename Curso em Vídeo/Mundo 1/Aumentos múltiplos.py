v = float(input('Qual o valor do salário? '))
if v >= 1250:
    ns = v + (v / 100 * 10)
    print('O novo salário será: {:.2f}R$'.format(ns))
else:
    ns = v + (v / 100 * 15)
    print('O novo salário será: {:.2f}R$'.format(ns))

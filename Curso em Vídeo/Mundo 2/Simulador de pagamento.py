print('='*50, 'Carvalho Modas', '='*50)
p = float(input('Qual será o valor do pagamento? '))
print('''
1. Dinheiro
2. Débito
3. Crédito''')
f = float(input('Qual será a forma de pagamento? '))
if f == 1:
    p1 = p / 100 * 90
    print('O valor da compra à vista é de R${:.2f}'.format(p1))
elif f ==2:
    p2 = p / 100 * 95
    print('O valor da compra no débito é de R${:.2f}'.format(p2))
elif f == 3:
    v = int(input('Quantas vezes será o crédito? '))
    if v <= 2:
        p3 = p / v
        print('O pagamento será de {} vez(es) de R${:.2f}'.format(v, p3))
    else:
        p3 = ((p / 100) * 120) / v
        print('O pagamento será de {} vezes de R${:.2f}'.format(v, p3))
else:
    print('Opção inválida, tente novamente.')

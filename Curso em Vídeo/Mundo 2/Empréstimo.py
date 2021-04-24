sal = float(input('Qual o salário da pessoa? '))
cas = float(input('Qual o valor da casa? '))
ano = int(input('Em quantos anos será pago essa casa? '))

per = ano * 12
pre = cas / per
p_sal = sal / 100 * 30

if p_sal > pre:
    print('Esse empréstimo tem um prazo de {} meses.'.format(per))
    print('E será pago em {} vezes de {:.2f}R$.'.format(per, pre))
    print('Ótimo, seu empréstimo estará aprovado com sucesso!')
else:
    print('O empréstimo não poderá ser efetuado. Pois ele excederia o valor de 30% do salário bruto.')

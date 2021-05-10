salario = float(input('Digite o valor do salário: '))
if salario <= 1903.98:
    print('Isento de Imposto de renda.')
elif salario >= 1903.99:
    print('Existe uma aliquota de 7,5% tendo a parcela de R$142,80.')
elif salario >= 3751.05:
    print('Há a aliquota de 15% tendo a parcela de R$354,80.')
elif salario >= 4664.68:
    print('Tem aliquota equivalente a 22,5% tendo parcela de R$636,13.')

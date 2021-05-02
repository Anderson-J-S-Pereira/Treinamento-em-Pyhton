sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
idade = int(input('Digite sua idade: '))

while sexo not in 'M, F':
    sexo = str(input('Dados inválidos, informe M ou F: ')).strip().upper()[0]

print('Sexo {} aceito com sucesso.'.format(sexo))
print('Idade {} aceita com sucesso.'.format(idade))

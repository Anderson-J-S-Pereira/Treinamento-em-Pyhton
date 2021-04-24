from datetime import date
atual = date.today().year
sexo = str(input('Qual o seu sexo? (Pressione F para feminino, pressione M para masculino): ')).upper().strip()
nasc = int(input('Qual foi o ano de nascimento? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos atualmente.'.format(nasc, idade))
if sexo == 'M':
    if idade == 18:
        print('Com essa idade, deve se alistar imediatamente, nesse ano de {}.'.format(atual))
    elif idade > 18:
        deveria_1 = idade - 18
        ano_1 = atual - deveria_1
        print('Com a idade atual, deveria ter se alistado há {} anos atrás. No ano de {}.'.format(deveria_1, ano_1))
    elif idade < 18:
        deveria_2 = atual + (18 - idade)
        ano_2 = atual + deveria_2
        print('Ainda não há a necessidade de alistamento com {} anos. O alistamento deve ocorrer no ano de {}.'.format(idade, deveria_2))
elif sexo == 'F':
    print('Não há a necessidade de alistamento obrigatório para pessoas do sexo feminino.')
else:
    print('Campo sexo preenchido incorretamente, tente novamente.')

n = str(input('Digite algo: '))
if n.isnumeric():
    print('É um número.')
else:
    print('Não é um número')
print('----------Fim----------')

i = int(input('Quantos anos completos você tem? '))
if i >= 18:
    print('É de maior.')
else:
    print('É de menor.')
print('-----Fim-----')

nota_1 = float(input('Qual a sua primeira nota? '))
nota_2 = float(input('Qual a sua segunda nota? '))
media = (nota_1 + nota_2) / 2
print('A sua nota foi: {:.1f}'.format(media))
if media >= 6:
    print('Parabéns! Foi aprovado.')
else:
    print('Não foi dessa vez. Rodastes! heuahuehae')

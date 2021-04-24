l_1 = float(input('Qual o tamanho do primeiro segmento? '))
l_2 = float(input('Qual o segundo segmento? '))
l_3 = float(input('Qual o terceiro segmento? '))

if l_1 > l_2 + l_3 or l_2 > l_1 + l_3 or l_3 > l_1 + l_2:
    print('Os valores dados, não é possível criar um triângulo.')
else:
    if l_1 == l_2 == l_3:
        print('Com os valores cedidos, é possível criar um triângulo equilátero.')
    elif l_1 != l_2 != l_3 != l_1:
        print('Com os valores cedidos, é possível criar um triângulo escaleno.')
    else:
        print('Com os valores cedidos, é possívl criar um triângulo isóceles.')

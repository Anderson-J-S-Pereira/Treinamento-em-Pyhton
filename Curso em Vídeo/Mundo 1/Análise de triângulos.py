t1 = float(input('Qual o valor do primeiro segmento? '))
t2 = float(input('Qual o valor do segundo segmento? '))
t3 = float(input('Qual o valor do terceiro segmento? '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Com os segmentos indicados, PODEM ser formados um triângulo.')
else:
    print('Com os segmentos indicados, NÃO podem ser formados um triângulo.')

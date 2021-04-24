'''import math
b = float(input('Qual o valor do cateto adjacente? '))
c = float(input('Qual o valor do cateto oposto? '))
a = (pow(b, 2) + pow(c, 2)) ** (1/2)
print('Com esses valores a hipotenusa é de aproximadamente {:.3f}'.format(a))'''

from math import hypot
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
hi = hypot(co, ca)
print('Com o valor de {} dado e do {} dado, a hipotenusa é: {:.3f}'.format(co, ca, hi))



import math
a = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tang = math.tan(math.radians(a))
print('De acordo com o ângulo {:.3f} que foi dado. Seu seno é {:.3f}, cosseno é {:.3f} e tangente é {:.3f}'.format(a, sen, cos, tang))

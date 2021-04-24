l = float(input('Qual a largura do retângulo? '))
a = float(input('Qual a altura do retângulo? '))
area = l * a
t = area / 2
print('Esse retãngulo tem {:.2f}m². E necessita de {:.2f} litros de tinta para pintar toda a sua área.'.format(area, t))
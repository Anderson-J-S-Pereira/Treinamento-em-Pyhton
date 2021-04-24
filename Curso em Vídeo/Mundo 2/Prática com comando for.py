from time import sleep
for oi in range(0 ,10):
    print('Oi!')
    sleep(0.3)
print('Fim')

for contagem in range(1 ,11):
    print(contagem)
    sleep(0.3)
print('Fim')

for cont in range(19, 0, -1):
    print(cont)
    sleep(0.3)
print('Fim')

n = int(input('Digite um valor: '))
for contador in range(0, n+1):
    print(contador)
    sleep(0.1)
print('Fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for con in range(i, f+1, p):
    print(con)
    sleep(0.2)
print('Fim')

import random
import time
itens = ('pedra', 'papel', 'tesoura')
comp = random.randint(0, 2)
print('''Suas escolhas:
0. Pedra
1. Papel
2. Tesoura''')
jog = (int(input('Escolha sua jogada: ')))
print('JO!')
time.sleep(0.5)
print('KEN!')
time.sleep(0.5)
print('PÔ!')
time.sleep(0.5)
print('=*='*20)
print('Sua escolha foi {}.'.format(itens[comp]))
print('A escolha do computador foi {}.'.format(itens[comp]))
print('=*='*20)
if comp == 0: #Computador escolheu pedra.
    if jog == 0:
        print('Empate!')
    elif jog == 1:
        print('Jogador venceu!')
    elif jog == 2:
        print('Máquina venceu!')
    else:
        print('Jogada inválida, tente novamente.')
elif comp == 1: #Computador escolheu papel.
    if jog == 0:
        print('Máquina venceu!')
    elif jog == 1:
        print('Empate!')
    elif jog == 2:
        print('Jogador venceu!')
    else:
        print('Jogada inválida, tente novamente.')
elif comp == 2: # Computador escolheu tesoura.
    if jog == 0:
        print('Jogador venceu!')
    elif jog == 1:
        print('Máquina venceu!')
    elif jog == 2:
        print('Empate!')
    else:
        print('Jogada inválida, tente novamente.')

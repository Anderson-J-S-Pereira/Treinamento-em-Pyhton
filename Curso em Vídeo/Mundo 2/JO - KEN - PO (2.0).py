from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
comp = randint(0, 2)
print('''Suas opções:
0. Pedra
1. Papel
2. Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('Jo...')
sleep(0.5)
print('Ken...')
sleep(0.5)
print('PÔ!!!')
sleep(1)
print('-=-' * 15)
print('O computador escolheu {}.'.format(itens[comp]))
print('Jogador escolheu {}.'.format(itens[jogador]))
print('-=-' * 15)
if comp == 0: # Comp jogou Pedra
    if jogador == 0: # Jogador jogou Pedra
        print('Ora ora, parece que houve um empate!')
    elif jogador == 1: # Jogador jogou Papel
        print('Jogador venceu!')
    elif jogador == 2: # Jogador jogou Tesoura
        print('Máquina venceu!')
    else: # Jogava inválida de jogador
        print('Jogada inválida, tente novamente.')
elif comp == 1: # Comp jogou Papel
    if jogador == 0: # Jogador jogou Pedra
        print('Máquina venceu!')
    elif jogador == 1: # Jogador jogou Papel
        print('Ora ora, parece que temos um empate!')
    elif jogador == 2: # Jogador jogou Tesoura
        print('Jogador venceu!')
    else: # Jogava inválida de jogador
        print('Jogada inválida, tente novamente.')
elif comp == 2: #Comp jogou Tesoura
    if jogador == 0: # Jogador jogou Pedra
        print('jogador venceu!')
    elif jogador == 1: # Jogador jogou Papel
        print('Máquina venceu!')
    elif jogador == 2: # Jogador jogou Tesoura
        print('Ora ora, parece que temos um empate!')
    else: # Jogava inválida de jogador
        print('Jogada inválida, tente novamente.')

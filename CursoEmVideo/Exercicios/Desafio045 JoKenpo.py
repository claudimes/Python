print('================= Desafio 45 =================')
print('============== Jogo Pedra - Papel - Tesoura ==============')
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas Opções:
( 0 ) PEDRA
( 1 ) PAPEL
( 2 ) TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador < 0 or jogador > 2:
    print("Jogada Invalida")
    exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0: # Computador Jogou Pedra
    if jogador == 0:
        print('EMPATE')
    else:
        if jogador == 1:
            print('JOGADOR VENCE')
        else:
            if jogador == 2:
                print('COMPUTADOR VENCE')
if computador == 1: # Computador Jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    else:
        if jogador == 1:
            print('EMPATE')
        else:
            if jogador == 2:
                print('JOGADOR VENCE')
if computador == 2: # Computador Jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    else:
        if jogador == 1:
            print('COMPUTADOR VENCE')
        else:
            if jogador == 2:
                print('EMPATE')



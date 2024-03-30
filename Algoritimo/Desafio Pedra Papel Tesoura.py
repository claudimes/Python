# Colaborou: Claudio Gomes, Thiago Prata e Joao Victor Machado

print('============== Jogo Pedra - Papel - Tesoura ==============')
from random import *
jogador = int(input('Digite Sua Jogada: '))
pc = randint(0,2)
# 0 = Pedra   ==> Ganha de Tesoura
# 1 = Papel   ==> Ganha de Pedra
# 2 = Tesoura ==> Ganha de Papel
print('Jogada PC: ', pc)
if jogador == 0 and pc == 1:
    print(f' Voce jogou {jogador} - Pedra e PC Jogou {pc} - Papel. PC Ganhou!')
else:
    if jogador == 1 and pc == 0:
        print(f'Voce jogou {jogador} - Papel e PC Jogou {pc} - Pedra. Voce Ganhou!')
    else:
        if jogador == 1 and pc == 2:
           print(f'Voce jogou {jogador} - Papel e o PC Jogou {pc} - Tesoura. PC Ganhou!')
        else:
            if jogador == 2 and pc == 1:
                print(f'Voce jogou {jogador} - Tesoura e o PC Jogou {pc} -  Papel. Voce Ganhou!')
            else:
                if jogador == 2 and pc == 0:
                    print(f'Voce jogou {jogador} - Tesoura e o PC Jogou {pc} - Pedra. PC Ganhou!')
                else:
                    if jogador == 0 and pc == 2:
                        print(f'Voce jogou {jogador} - Pedra e o PC Jogou {pc} - Tesoura. PC Ganhou!')
                    else:
                        if pc == jogador:
                            print('Jogadas Iguais - Empate')
                        else:
                            if jogador < 0 or jogador > 2:
                                print('Jogada Invalida')
















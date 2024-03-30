# Colaborou: Claudio Gomes, Thiago Prata e Joao Victor Machado

import random
from time import sleep

print('-=-' * 20)
print('\033[1;35m Sou seu COMPUTADOR... Acabei de pensar em um numero de 0 a 1.000.000')
print('Será que consegue adivinhar qual foi?\033[m')
print('-=-' * 20)
palpites = 0
computador = random.randint(0, 1000000)
# print(f'Computador: {computador}')
while True:
    sleep(1)
    jogador = int(input('\033[1;36mQual seu palpite? : \033[m'))
    print('\033[1;31m PROCESSANDO... \033[m')
    sleep(1)
    palpites += 1
    if computador == jogador:
        break
    else:
        if jogador < computador:
            print('\033[1;33m Mais... Tente mais uma vez.\033[m')
        else:
            print('\033[1;33m Menos... Tente mais uma vez.\033[m')
print(f'\033[1;32m Na Mosca! Acertou com {palpites} palpites. PARABENS!!! \033[m')

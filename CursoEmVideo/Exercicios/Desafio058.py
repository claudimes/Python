import random
from time import sleep
print ('================= Desafio 58 =================')
print(' ')
print('-=-' * 20)
print('Sou seu computador... Acabei de pensar em um numero de 0 a 10.')
print('Será que consegue adivinhar qual foi?')
print('-=-' * 20)
acertou = False
palpites = 0
while  not acertou:
    computador = random.randint(0, 10)
    jogador = int(input('Qual seu palpite? : '))
    print('PROCESSANDO...')
    sleep(1)
    palpites += 1
    if computador == jogador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print(f'Acerto com {palpites} palpites. PARABENS!')

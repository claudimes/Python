import random
from time import sleep
print ('================= Desafio 28 =================')
print(' ')
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? : '))
print('PROCESSANDO...')
sleep(3)
compurador = random.randint(0,5)
if compurador == jogador:
    print('PARABENS! Você consegiu me Vencer!')
else:
    print(f'GANHEI! Eu pensei no numero {compurador} e não no {jogador}.')

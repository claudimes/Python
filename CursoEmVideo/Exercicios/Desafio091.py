'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4' : randint(1, 6)}
ranking = []
print('Valores Sorteados:')
for k, v in jogo.items(): # K=Key(Chave)  V=Valores(valor)
        print(f'{k} tirou {v} no dado.')
        sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)#Precisa importar itemgetter
# para escolher a posição, Como estava exibindo por ultimo, incluiu o Reverse
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):# I= Indice V=Valor
        print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')



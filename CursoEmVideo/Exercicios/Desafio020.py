print ('================= Desafio 20 =================')
'''import random
a1 = input('Digite o Primeiro Aluno: ')
a2 = input('Digite o Segundo Aluno: ')
a3 = input('Digite o Terceiro Aluno: ')
a4 = input('Digite o Quarto Aluno: ')
lista = [a1 , a2 , a3 , a4]
random.shuffle (lista)
print('A Orfem da Apresentação será')
print(lista)'''

#Forma de Função unica Utilizada.

from random import shuffle
a1 = input('Digite o Primeiro Aluno: ')
a2 = input('Digite o Segundo Aluno: ')
a3 = input('Digite o Terceiro Aluno: ')
a4 = input('Digite o Quarto Aluno: ')
lista = [a1 , a2 , a3 , a4]
shuffle (lista)
print('A Orfem da Apresentação será')
print(lista)
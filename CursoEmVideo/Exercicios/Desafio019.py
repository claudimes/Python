print ('================= Desafio 19 =================')
import random
a1 = input('Digite o Primeiro Aluno: ')
a2 = input('Digite o Segundo Aluno: ')
a3 = input('Digite o Terceiro Aluno: ')
a4 = input('Digite o Quarto Aluno: ')
lista = [a1 , a2 , a3 , a4]
sorteio  = random.choice (lista)
print(f'O Aluno escolhido foi: {sorteio}')


''' Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
que estão na tupla.'''
from random import randint
numeros = (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10))
print(f'Os valores sorteados foram :{numeros}')
for n in numeros:#outra forma de exibição
    print(f'{n}', end=' ')

print(f'\n O maior valor sorteado foi: {max(numeros)}')#max mostra o maior numero da Tulpa
print(f'O menor valor sorteado foi: {min(numeros)}')#min monstra o menor numero da Tupla



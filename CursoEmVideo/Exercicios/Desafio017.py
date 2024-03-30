print ('================= Desafio 17 =================')
'''import math
cateto_oposto = float(input('Qual é o comprimento do Cateto oposto? '))
cateto_adjacente = float(input('Qual é o comprimento do Cateto Adjacente? '))
hipotenusa = math.hypot(cateto_oposto , cateto_adjacente)
print(f'A medida da Hipotenusa é: {hipotenusa :.2f}.')

Outra Forma de Fazer somete com a Função Especifica.'''
from math import hypot
cateto_oposto = float(input('Qual é o comprimento do Cateto oposto? '))
cateto_adjacente = float(input('Qual é o comprimento do Cateto Adjacente? '))
hipotenusa = hypot(cateto_oposto , cateto_adjacente)
print(f'A medida da Hipotenusa é: {hipotenusa :.2f}.')

'''Forma Sem Importação de Biblioteca

cateto_oposto = float(input('Qual é o comprimento do Cateto oposto? '))
cateto_adjacente = float(input('Qual é o comprimento do Cateto Adjacente? '))
#hipotenusa = pow(cateto_oposto , 2) + pow(cateto_adjacente , 2)
print(f'A medida da Hipotenusa é: {(cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2) :.2f}.')'''

''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

n = int(input('Digite um Numero: '))
r = 0
for i in range(1,n+1):
    if n % i == 0:
        r += 1
if r == 2:
    print(f'O Numero {n} é PRIMO.')
else:
    print(f'O Numero {n} é NÃO é Primo.')


# 9.Escrever o algoritmo que leia os valores n1 e n2 e imprima o intervalo fechado  (incluindo os
# (limites) entre esses dois valores.

n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º número: '))
print(f'O Intervalo entre {n1} e {n2} é:.')
if n1 < n2:
    for i in range (n1 + 1 , n2):
        print(f' {i}',end=(''))
else:
    if n2 < n1:
        for i in range(n1 - 1 , n2, -1):
            print(f' {i}', end=(''))

'''Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
'''O For de alimentação'''
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
''''o mesmo For, agora são estrutura de repetição para mostrar a estrutura na tela'''
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


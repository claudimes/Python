''' Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.'''

maior_peso = 0
menor_peso = 0
for i in range(1, 6):
    peso = float(input(f'Peso da {i} pessoa: '))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if maior_peso < peso:
            maior_peso = peso
        if menor_peso > peso:
            menor_peso = peso
print(f'O MAIOR peso foi {maior_peso} Kg.')
print(f'O MENOR peso foi {menor_peso} Kg.')

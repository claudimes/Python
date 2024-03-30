maior = 0
menor = 0

for i in range(1, 21):
    n = float(input(f'Digite o {i}º Numero: '))
    if i == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'O Maior numero lido foi {maior}')
print(f'O Menor numero lido foi {menor}')

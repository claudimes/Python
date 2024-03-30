'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''

valores = []
maior = menor = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um Valor para a Posição {c}. ')))
    if c == 0:
        maior = menor = valores[c]#pega o valor posição [C]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'O Maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end=' ')
print(f'\n O Menor valor digitado foi: {menor} na Posição', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end=' ')

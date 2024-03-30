'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    lista.append(int(input('Digite um Valor: ')))
    resp = '1'
    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja continar? [S]/[N] ')).upper().strip()
    if resp == "N":
        break
print('-=' * 30)

lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 NÃO foi encontrado na lista.')



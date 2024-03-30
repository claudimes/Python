''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
 se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

print('-' * 25)
print('LOJA SUPER BARATÃO')
print('-' * 25)
totcompra = maior_mil = pre_prod_mb = cont = 0
prod_mais_bar = ' '
while True:
    cont += 1
    produto = str(input('Nome do PRODUTO: ')).upper().strip()
    preco = float(input('PREÇO: R$ '))
    totcompra += preco
    if cont == 1 or preco < pre_prod_mb:
        prod_mais_bar = produto
        pre_prod_mb = preco
    if preco >= 1000:
            maior_mil += 1
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'TOTAL gasto na compra R$ {totcompra:.2f}')
print(f'Temos {maior_mil} produtos custando mais de R$ 1.000,00.')
print(f'O produto mais BARATO foi: {prod_mais_bar} e custou R$ {pre_prod_mb:.2f}.')
print('{:-^40}'.format('FIM DO PROGRAMA'))










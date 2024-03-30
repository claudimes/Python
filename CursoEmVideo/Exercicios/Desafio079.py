''' Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''
lista = []

while True:
    num = (int(input('Digite um valor: ')))
    if num in lista:
        print('Valor Duplicado! Não Vou adicionar...')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    resp = '1'
    while resp != "S" and resp != 'N':
        resp = str(input('Deseja continuar? [S]/[N] ')).upper().strip()
    if resp == 'N':
        break
lista.sort()
print(f'Você digitou os valores: {lista}.', end=' ')


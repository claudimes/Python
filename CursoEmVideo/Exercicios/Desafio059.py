''' Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
valor_1 = 0
valor_2 = 0
resposta = 0
c = 0
while resposta != 5:
    valor_1 = int(input('Digite o 1º Numero: '))
    valor_2 = int(input('Digite o 2º Numero: '))
    print(''' O que Deseja Fazer? 
    [1] SOMAR
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa''')
    resposta = int(input('Digite um OPÇÃO: '))
    if resposta == 1:
        print(f'A SOMA de {valor_1} + {valor_2} = ', valor_1 + valor_2)
    else:
        if resposta == 2:
            print(f'A MULTIPLICAÇÃO de {valor_1} x {valor_2} = ', valor_1 * valor_2)
        else:
            if resposta == 3:
                if valor_1 > valor_2:
                    print(f'O MAIOR Valor Digitado entre: {valor_1} e {valor_2} é: ', valor_1)
                else:
                    if valor_2 > valor_1:
                        print(f'O MAIOR Valor Digitado entre: {valor_1} e {valor_2} é: ', valor_2)
                    else:
                        print(f'Os Números: {valor_1} e {valor_2} são IGUAIS. ')
            else:
                if resposta == 4:
                    print('Informe os numeros novamente:')
                    valor_1 = int(input('Digite o 1º Numero: '))
                    valor_2 = int(input('Digite o 2º Numero: '))
                else:
                    if resposta == 5:
                        print('Finalizando...')
                    else:
                        print(f'{resposta} é uma opção invalidade. Tente novamente!')
    sleep(2)
print('Fim do programa. Volte Sempre!')


'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''

from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 15)
vitoria = 0
while True:
    jogador = ' '
    num = int(input('Digite um valor: '))
    pc = randint(0, 10)
    resultado = (num + pc)
    while jogador not in 'PI':
        jogador = str(input('Par ou Imparar.[P/I]: ')).upper().strip()[0]
    if resultado % 2 == 0:
        if jogador == 'P':
            print('Voce VENCEU!')
            vitoria += 1
        else:
            if jogador == 'I':
                print('Voce PERDEU!')
                break
        print(f'Você jogou {num} e o Computador {pc}. Total de {resultado} DEU PAR.')
    else:
        if jogador == 'I':
            print('Você VENCEU!')
            vitoria += 1
        else:
            if jogador == 'P':
                print('Você Perdeu!')
                break
        print(f'Você jogou {num} e o Computador {pc}. Total de {resultado} DEU IMPAR.')
    print('-' * 40)
    print('Vamos jogar novamente ...')
print('-' * 40)
print(f'GAME OVER! Você venceu {vitoria} vezes.')

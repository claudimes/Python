'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

numero = cont = soma = 0
while numero != 999:
    numero = int(input('Digite um Numero: [999 para parar] '))
    if numero == 999:
        print('TERMINOU')
    else:
        cont += 1
        soma += numero
print(f'Voce digitou {cont} NÚMEROS.')
print(f'Sua SOMA é de : {soma}.')




'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

resposta = 'S'
cont = media = maior = menor = 0
while resposta != 'N':
    numero = int(input('Digite um NÚMERO: '))
    cont += 1
    media += numero
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar a Digitar Valores? [S]/[N]: ')).upper().strip()[0] #so pega a 1º letra
print(f'Voce digitou {cont} NUMEROS e a  MEDIA foi: {media / cont:.2f}')
print(f'O MAIOR valor é: {maior} e o MENOR é: {menor}.')





'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.'''

primeiro = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão: '))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo + 1, razao):
    print(i, end=" ")

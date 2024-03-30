'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. '''

while True:
    num = int(input('Quer ver a Tabuada de qual valor? '))
    print('-' * 35)
    if num < 0:
        break
    for cont in range(1,11):
        print(f'{num} x {cont} = ', num * cont)
    print('-' * 35)
print('PROGRAMA DE TABUADA ENCERRADO. Volte Sempre!')


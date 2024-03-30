#10.Escrever um algoritmo que leia um número n que indica quantos valores devem ser lidos a
# seguir. Para cada número lido, mostre o valor lido e o fatorial deste valor.

numero = int(input('Digite quantos valores devem ser lidos: '))
if numero < 0:
    print(f'O NÚMERO {numero} é Invalido!')
else:
    factorial = 1
    for c in range (numero, numero * 2 + 1):
        factorial = factorial * c
        print(f'O NÚMERO lido é {c}. Seu FACTORIAL de {c}! é: {factorial}')

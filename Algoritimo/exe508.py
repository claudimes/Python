'''Escreva uma função que receba como parâmetro um valor n inteiro e positivo e que calcule a seguinte
 soma:S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n. A função deverá retornar o valor de S'''
def calculo(num):
    soma = 0
    for s in range(1, num + 1):
        soma += 1 / s
    return soma


num = int(input('Digite um NÚMERO: '))

print(f'S = {calculo(num):.2f}')

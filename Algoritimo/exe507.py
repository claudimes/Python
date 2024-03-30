'''Escrever uma função somarIntervalo(n1, n2) que retorna a soma dos números inteiros que existem entre
 n1 e n2 (inclusive ambos). A função deve funcionar inclusive se o valor de n2 for menor que n1. '''

def somaintervalo(n1, n2):
    soma = 0
    if n1 < n2:
        for s in range(n1, n2 + 1):
            soma += s
    else:
        for s in range(n2, n1 + 1):
            soma += s
    return soma


n1 = int(input('Digite o 1º NÙMERO: '))
n2 = int(input('Digite o 2º NÚMERO: '))

print(f'A SOMA entre os Intervalos {n1} e {n2} = {somaintervalo(n1, n2)}')


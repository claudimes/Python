'''Escrever uma função contarImpar(n1, n2) que retorna o número de inteiros ímpares
 que existem entre n1 e n2 (inclusive ambos, se for o caso). A função deve funcionar inclusive se o
 valor de n2 for menor que n1'''

def contarImpar(n1,n2):
    n_i = []
    if n1 < n2:
        for i in range(n1, n2 + 1):
            if i % 2 != 0:
                n_i.append(i)
    else:
        n_i = []
        for i in range(n2, n1 + 1):
            if i % 2 != 0:
                n_i.append(i)
    n_i.sort(reverse=True)
    return n_i


n1 = int(input('Digite o 1º Número: '))
n2 = int(input('Digite o 2º Número: '))
print(f'NÚMEROS IMPAR dentro Intervalo de {n1} e {n2}: {contarImpar(n1, n2)}')


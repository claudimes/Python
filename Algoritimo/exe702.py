# 2.	Faça uma função que recebe, por parâmetro, uma
# matriz 6x6 e retorna a soma dos elementos da sua diagonal
# principal e da sua diagonal secundária.

def somar_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma = soma + matriz [i][i]
    return soma

def somar_diagonal_secundaria(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma = soma + matriz [i][len(matriz) - i - 1]
    return soma

matriz = [
    [ 1,  2,  3,  4,  5,  8],
    [ 7,  8,  9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
]

print(somar_diagonal_principal(matriz))
print(somar_diagonal_secundaria(matriz))
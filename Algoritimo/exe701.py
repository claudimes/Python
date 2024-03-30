# 1.	Faça uma função que recebe, por parâmetro,
# uma matriz 5x5 e retorna a soma dos seus elementos.

def somar_matriz(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = soma + matriz [i][j]
    return soma

matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
    [0, 9, 8, 7, 6],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [1, 1, 1, 1, 1]
]

print(somar_matriz(matriz))
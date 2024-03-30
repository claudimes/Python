'''Escrever uma função que recebe por parâmetro um vetor de inteiros e
retorna a soma de seus elementos'''

# def soma_num(num):
#     soma = 0
#     for s in range(len(num)):
#         soma += num[s]
#     return soma
#
# num = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]
# print(f'A SOMA de seus elementos é: {soma_num(num)}.')
'''Versão Professor'''


def somar(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma = soma + vetor[i]
    return soma


vetor = [5, 3, 2, 4, 9, 8, 7, 0, 1, 6]

print(somar(vetor))

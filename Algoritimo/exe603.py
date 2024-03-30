'''Implemente uma função que retorne o menor elemento de um vetor de inteiros. '''

# def verifica_maior(vetor):
#     menor = vetor[0]
#     for n in range(len(vetor)):
#         if vetor[n] < menor:
#             menor = vetor[n]
#     return menor
#
#
# vetor = [-2, -4, -7, -8, -12]
# print(f'O MENOR elemento do vetor é: {verifica_maior(vetor)}.')
'''Versão Professor'''
def encontrar_menor_valor(valores):
    menor = valores[0]
    for i in range(len(valores)):
        if valores[i] < menor:
            menor = valores[i]
    return menor

vetor = [-9, -8, -5, -3, -10, -20, -1]
print(f"Menor valor = {encontrar_menor_valor(vetor)}")

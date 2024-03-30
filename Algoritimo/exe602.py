'''Implemente uma função que retorne o maior elemento de um vetor de inteiros. '''

# def verifica_maior(vetor):
#     maior = vetor[0]
#     for n in range(len(vetor)):
#         if vetor[n] > maior:
#             maior = vetor[n]
#     return maior
#
#
# vetor = [50, 2, 7, 9, 10, 12]
# print(f'O MAIOR elemento do vetor é: {verifica_maior(vetor)}.')
'''Versão Professor'''
def encontrar_maior_valor(valores):
    maior = valores[0]
    for i in range(len(valores)):
        if valores[i] > maior:
            maior = valores[i]
    return maior

vetor = [-9, -8, -5, -3, -10, -20, -1]
print(f"Maior valor = {encontrar_maior_valor(vetor)}")

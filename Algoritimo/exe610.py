'''Escrever uma função que substitui por zero todos os números negativos do vetor passado por parâmetro'''


def substituir_zero(vetor):
    for i in range(len(vetor)):
        if vetor[i] < 0:
            vetor[i] = 0

    return vetor


vetor = [2, 4, 3, 6, -1, -3, 8, -1, 4]
print(substituir_zero(vetor))
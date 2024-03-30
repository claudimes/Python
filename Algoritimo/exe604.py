'''Implemente uma função que ordene um vetor de inteiros de tamanho 10'''

def ordenar(vetor):
    for i in range(len(vetor)):
        for j in range(i, len(vetor)):
            if vetor[j] < vetor[i]:
                aux = vetor[j]
                vetor[j] = vetor[i]
                vetor[i] = aux
    return vetor


vetor = [5, 3, 2, 4, 9, 8, 7, 0, 1, 6]
print(ordenar(vetor))

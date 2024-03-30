#5.	Faça uma função recursiva que receba um vetor de números inteiros e seu tamanho e
# retorne a soma de seus elementos.

def soma(vetor, tamanho):
    if tamanho != 0:
        soma(vetor, tamanho - 1)

    if tamanho != len(vetor):
        teste = vetor[tamanho]
    return teste


vetor = [1, 2, 3, 4]
tamanho = len(vetor)
soma(vetor, tamanho)


'''Escrever uma função que receba um vetor com 10 valores e retorne quantos destes valores
 são negativos'''
def contar_negativos(valores):
    quantidade_negativos = 0
    for i in range(len(valores)):
        if valores[i] < 0:
            quantidade_negativos = quantidade_negativos + 1
    return quantidade_negativos

vetor = []
quantidade = int(input("Quantos valores deseja fornecer? "))
for i in range(1,quantidade + 1):
    valor = int(input(f"Digite o valor {i}: "))
    vetor.append(valor)

print(f"Quantidade de negativos = {contar_negativos(vetor)}")
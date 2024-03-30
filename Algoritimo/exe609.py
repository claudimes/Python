'''Implemente uma função que retorne a média dos valores armazenados em um vetor de inteiros. '''

# def media_valores(valor):
#     cont = s = 0
#     for c in range(len(valor)):
#         cont += 1
#         s += valor[c]
#     media = (s / cont)
#     return media
# # Modo Rapido
# # valor = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# #Modo pelo usuario
# valor = []
# resp = int(input('Quantos Valores que informar? '))
# for p in range(1, resp+1):
#     valor.append(int(input(f'Digite o {p}º Numero: ')))
# print(f'A MEDIA dos Valores Armazenados é: {media_valores(valor)}')
'''Versão Professor'''
def calcular_media(vetor):
    soma = 0
    media = 0
    for i in range(len(vetor)):
        soma = soma + vetor[i]
    if len(vetor) != 0:
        media = soma / len(vetor)

    return media


vetor = [2, 4, 3, 6]
print(calcular_media(vetor))




'''Implemente uma função que, dado um valor, retorne se esse valor pertence ou não a um
vetor de inteiros. '''
#
# def pertence(num):
#     if num in inteiro:
#         resp = 'Sim'
#     else:
#         resp = 'Não'
#     return resp
#
# inteiro = [1, 10, 30, 35, 45, 50]
# num = int(input('Digite um número: '))
# print(f'O Número {num} pertence a Lista? {pertence(num)}')

'''Versão Professor'''

def verificar_lista(lista, numero):
    i = 0
    encontrou = False
    while i < len(lista) and not encontrou:
        if lista[i] == numero:
            encontrou = True
        i = i + 1
    return encontrou

lista = [1, 3, 5, 7, 9]

print (verificar_lista(lista, 3))


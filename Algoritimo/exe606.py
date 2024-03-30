'''Escrever a função que recebe por parâmetro uma string e um número.
A função deve retornar os primeiros caracteres da string de acordo com o número passado por parâmetro. '''

# def primeiro_caracter(nome, num):
#     prim = []
#     for i in range(len(nome)):
#         if i <= num:
#             prim.append(nome[i])
#     return prim
#
#
# nome = str(input('Digite um NOME: ')).upper().strip()
# num = int(input('Digite um NÚMERO: '))
# if num > len(nome):
#     print(f'NÚMERO Invalido! Favor digitar um valor até {len(nome)}.')
#     num = int(input('Digite um NÚMERO: '))
#
# print(primeiro_caracter(nome, num))
'''Versão Professor'''


def retornar_primeiros_caracteres(palavra, quantidade):
    resultado = ""
    for i in range(quantidade):
        resultado = resultado + palavra[i]
    return resultado


palavra = "algoritmos"
quantidade = 3
print(retornar_primeiros_caracteres(palavra, quantidade))









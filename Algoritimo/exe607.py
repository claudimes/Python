'''Escrever a função que recebe por parâmetro uma string e um caracter.
e a função deve retornar os primeiros caracteres da string até encontrar
o caracter passado por parâmetro'''

# def string_carac():
#     resp = ''
#     while carac not in resp:
#         for l in nome:
#             resp += l
#             if l == carac:
#                 break
#     return resp
#
#
# nome = str(input('Digite uma Palavra: ')).upper().strip()
# carac = str(input('Digite um Caracter[letra]: ')).upper().strip()[0]
# if carac not in nome:
#     print('NÂO Gostei desse Caracter! Tente outro...')
#     carac = str(input('Digite um Caracter[letra]: ')).upper().strip()[0]
#
# print(f'Primeiros caracteres da string até o caracter é: ',{string_carac()})
'''Versão Professor'''


def imprimir_ate_letra(palavra, letra):
    i = 0
    parar = False
    resultado = ""
    while i < len(palavra) and not parar:
        if palavra[i] == letra:
            parar = True
        resultado = resultado + palavra[i]
        i = i + 1
    return resultado


palavra = str(input('Digite uma Palavra: ')).upper()
letra = str(input('Qual Letra? ')).upper().strip()[0]
print(imprimir_ate_letra(palavra, letra))

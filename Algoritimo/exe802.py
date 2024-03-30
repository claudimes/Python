#2.	Faça uma função recursiva para exibir na tela os números ímpares de 1 a 30.

def imprimir(numero):
    if numero != 1:
        imprimir(numero - 1)
    if numero % 2 != 0:
        print(numero)


imprimir(30)

# 1.	Faça uma função recursiva para exibir na tela de 1 a 10.

def imprimir(numero):
    #print(numero) # Decrescente

    if numero != 0:
        imprimir(numero - 1)

    print(numero) #Crescente

imprimir(10)
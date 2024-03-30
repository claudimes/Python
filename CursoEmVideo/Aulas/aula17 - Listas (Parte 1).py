num = [2, 5, 9, 1]
num[2] = 3
num.append(7) #append adicona valores(estou adicionado o valor 7 ao elemento)
num.sort() #sort coloca os valores em ordem crescente
print(num)
num.insert(2, 0) #Na Posição 2 Iserir o valor 0. O Python refaz o indice automatico.
num.sort(reverse=True) #sort(reverse=True) coloca os valores em ordem decrescente
print(num)
print(f'Esta lista tem {len(num)} elementos.') # Função Len retorna quantos elementos tem.
# num.pop() # Pop() sem parametros, elimina o ultimo valor.
'''Testes para evitar erro em uma função'''
if 4 in num:
    num.remove(5) # Remove procura do Incio da lista a primeira ocorrencia que pediu para elinimar. Ele não varre ate o final
else:
    print('Não achei o numero 5')
print(num)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
# for v in valores:
#     print(f'{v}...', end=" ")
for c, v in enumerate(valores): #enumerate pega tanto a chave e o valor.
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores): #enumerate pega tanto a chave e o valor.
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a [:] # [:] faz um backup se a. Na verde ele cria uma copia de A.
b[2] = 8 #Altera a posição 2 para 8 incluive na lista A, aprtir do momento que iguala uma lista a outra,
# o Pythom cria uma ligação entre elas.
print(f'Lista A: {a}')
print(f'Lista B: {b}')




lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas São Imutaveis

print(len(lanche))#len contador de itens na Tupla
print('~' *30)
#Se eu não precisar me dar a posição. Maneira mais simples.
for c in lanche:#For(Para) itens, Repetição(Interação),
    print(f'Eu vou comer {c}.')
print('~' *30)
#Se precisar de posição, Pode usar das duas maneiras
for pos, c in enumerate(lanche):#enumerate, alem do dado me da a posição com as 2 variaveis.
    print(f'Eu vou comer {c} na posição {pos}.')
print('~' *30)

for cont in range(0, len(lanche)):#O Range vai começar no 0 e volta ate o fim. lembrando que o range ignora o ultimo
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')#mesma coisa que o For de cima/Mesmo Resultado, Aqui uso o range, em cima usou a Variavel Composta

print('Comi pra caramba!')
#sorted siginifica organizado(em ordem)
print(sorted(lanche))
print(lanche)

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = b + a#Junta(Cola) as 2 Tuplas, aqui a ordem tem TOTAL influencia
# print(c)
# print(len(c))
# print(c.count(5))#Quantas vez o numero aparece na Tupla
# print(c.index(2))#Que Posição esta o 2?Pega a primeira posição

pessoa = ('Gustavo', 39, 'M', 99.98)
# del(pessoa)#Quando uso del, voce apaga uma variavel. Apaga ela toda.
print(pessoa)



# teste = []
# teste.append('Gustavo')
# teste.append(40)
# galera = []
# galera.append(teste[:])#[:] cria um backup da lista teste ate aquele momento
# teste[0] = 'Maria'
# teste[1] = '22'
# galera.append(teste[:])
# print(galera)
'''------------------------------------------------------------------------------------------------------------------'''
# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# print(galera)#Mostra Todo Mundo
# print(galera[0]) #Seria me mostrar todos os dados do João
# print(galera[0][0])# Vou pegar o galera 0(que é o Joao 19), vou pegar o primeiro item que é Joao
# print(galera[2][1])# Vou pegar o galera 2(que é o Joaquim 13), vou pegar o segundo item que é 13

# for p in galera:#Para(for) cada pessoa(p) in(dentro) galera,
#     print(f'{p[0]} tem {p[1]} anos de idade.')
'''O que eu fiz. Criei 2 estruturas.
Essa estrutura de dado vai ser uma estrutura auxiliar, que eu vou pegar os dados pata depois ir para a estrutura
principal que é a galera'''

galera = []
dado = []
totmai = totmen = 0# Vou ver o maior e menor de idade

'''Esse bloco aqui todo é para eu ler os dados e jogar dentro da galera, apagando os dados a cada vex que eu faço o laço'''
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])#Vou pegar esses dado e jogar dentro da galera com uma copia do dado
    dado.clear()#Apagando os dados a cada vez que eu faço o laço

'''Aqui eu analiso para saber se o cara é maior ou menor de idade e ja vou totalizando para mostar'''
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idades')








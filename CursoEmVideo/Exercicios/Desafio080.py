'''Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''

lista = []
for c in range(0, 5):
    num = (int(input('Digite um valor: ')))
    if c == 0 or num > lista[-1]:#Se ele for o primeiro ou Então se ele for Maior que o Ultimo valor
        lista.append(num)
        print(f'Adicionado ao final da lista...')
    else:#Tenho que descobri que posição vou adicionar, vou varrer o vetor inteiro
        pos = 0#Pos = Posição
        while pos < len(lista):# Isso é, ele vai da posição 0 ate a ultima posição
            if num <= lista[pos]:#Vou verificar se o num que vou inserir é menor ou igual a lista na posição POs
                # Eu vou verificar dentro de cada posição se o numero que eu quero inserir é menor ou igual a ele.
                #Se ele for, eu vou inserir em uma posição especifica, ai não vou usar o appendi e sim o insert
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores informados em ordem foram {lista}')

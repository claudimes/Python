pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

# for k in pessoas.keys():
#     print(k)

# for k in pessoas.values():
#     print(k)
# pessoas['nome'] = 'Leandro' # Usando para alterar um elemento
# pessoas['peso'] = 98.5 # Usado para Adicionar um elemento
# # del pessoas['sexo'] Apaga aquele item(elemento)
# for k, v in pessoas.items(): # Nos dicionarios não tem o uso do enumereite, se usa esse comando .items
#     print(f'{k} = {v}')

'''Criando um Dicionario dentro de uma Lista'''
# brasil = []
# estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
# estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
#
# print(brasil)
# print(brasil[0])
# print(brasil[1])
# print(brasil[0]['UF'])
# print(brasil[1]['Sigla'])
'''------------------------------------------------------------------------------------------------------------'''
estado = {}
brasil = []
for c in range(0, 1):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) #Essa é a forma de fazer copia em Dicionario
for e in brasil:# Laço da Lista, onde e passa assunmir os nomes no laço
    for v in e.values():#Pode usar o Items ou Keys. Depende do que vai precisar
        print(v, end=" ")
    print()








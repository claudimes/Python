'''Faça um programa que leia nome e média de um aluno, guardando também a
situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
if aluno['Media'] >= 7:
    aluno['Situaçao'] = "Aprovado"
else:
    if aluno['Media'] >=5 :
        aluno['Situaçao'] = 'Recuperação'
    else:
        if aluno['Media'] < 5:
            aluno['Situaçao'] = 'Reprovado'
# print(f'O Nome é {aluno["Nome"]}')
# print(f'A media é igual a {aluno["Media"]}')
# print(f'Situação é igual á {aluno["Situaçao"]}.')
print('-=' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')

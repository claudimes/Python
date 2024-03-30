''' Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. '''

from datetime import date
ano_atual = date.today().year
maior_idade = 0
menor_idade = 0
for i in range(1, 8):
    ano_nascimento = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        maior_idade += 1
    else:
        menor_idade += 1
print(f"{menor_idade} pessoas NAO atingiram a maior idade.")
print(f"{maior_idade} pessoas SÃO maior idade.")


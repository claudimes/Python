'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)
soma_idade = soma_homens = soma_mulheres = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: [M]/[F]: ')).upper().strip()[0]
    if idade >= 18:
        soma_idade += 1
    if sexo == 'M':
        soma_homens += 1
    if sexo == 'F' and idade < 20:
        soma_mulheres += 1
    resposta = ' '
    while resposta not in 'NS':
        resposta = str(input('Deseja continuar: [S]/[N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
    print('-' * 20)
print(f'Total de pessoas com mais de 18 anos: {soma_idade}.')
print(f'Ao todo temos {soma_homens} homens cadastrados.')
print(f'E temos {soma_mulheres} mulheres com menos de 20 anos.')






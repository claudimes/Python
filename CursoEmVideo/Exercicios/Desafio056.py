''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e
quantas mulheres têm menos de 20 anos. '''
media = 0
c = 0
idade_hv = 0
velho = ' '
idade = 0
mulheres_menores = 0
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input('NOME: ')).upper().strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO. [M]/[F]: ')).upper().strip()
    c += 1
    media += idade
    if i == 1 and sexo == 'M':
        idade_hv = idade
        velho = nome
    if sexo == 'M' and idade > idade_hv:
        velho = nome
        idade_hv = idade
    if sexo == 'F' and idade < 20:
        mulheres_menores += 1
print(f'A media da IDADE do Grupo é {media/c:.2f} anos. ')
print(f'O HOMEM mais VELHO tem {idade_hv} anos é se chama {velho}.')
print(f'Ao todo são {mulheres_menores} mulheres com MENOS de 20 anos.')

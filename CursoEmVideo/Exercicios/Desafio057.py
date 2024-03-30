'''  Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto. '''

sexo = str(input('Infome seu Sexo. [M[/[F]: ')).upper()[0].strip()#Maicula/elimina espaço e pega a 1º letra
while sexo not in 'MF':
    sexo = str(input('Dados invalidos.Por favor Informe seu Sexo. [M[/[F]: ')).upper()[0].strip()
print(f'Sexo {sexo} resgistrado com sucesso!')




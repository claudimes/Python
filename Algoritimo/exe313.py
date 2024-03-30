numero = 1
contador = 0
soma = 0
soma_par = 0
par = 0
impar = 0
while numero != 0:
    numero = int(input('Digite um Numero POSITIVO: '))
    if numero < 0:
        print('Não é PERMITIDO numero NEGATIVO!')
    else:
        if numero == 0:
            print('FIM')
        else:
            contador = contador + 1
            soma = soma + numero
            if numero % 2 == 0:
                par = par + 1
                soma_par = soma_par + numero
            else:
                impar = impar + 1

media_geral = soma / contador
media_par = soma_par / par
print(f'Quantidade de números PARES: {par}.')
print(f'Quantidade de números IMPARES: {impar}.')
print(f'Média de valores PARES: {media_par}.')
print(f'Média geral dos números lidos: {media_geral}.')

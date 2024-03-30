''' Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. '''
frase = str(input('Digite uma frase: ')).strip().upper() #Tira espaço e Fica MAIUSCULA
palavras = frase.split() # Dividi as Palavras
junto = ''.join(palavras) # Junta Todas as Palavras eliminando os espaços, ou pode incluir outro caracter
inverso = ''
for letra in range(len(junto) - 1, -1,-1):# len pega a ultima letra, tira 1, e vai voltando 1 letra
    inverso += junto[letra]
print(f'O Inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada NAO é um palíndromo!')


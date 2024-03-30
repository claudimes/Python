soma = 0
contador = 0
positivo = 0
negativo = 0
continua = "S"

while continua == 'S':
    n = int(input('Digite um número: '))
    contador = contador + 1
    soma = soma + n
    if n > 0:
        positivo = positivo + 1
    else:
        negativo = negativo + 1

    continua = str(input('Deseja continuar? (S)/(N): ')).upper()
    if continua != 'N' and continua != 'S':
        print('Resposta INVALIDA. Tente Novamente!')

media = soma / contador
percentual_posito = (positivo * 100) / contador
percentual_negativo = (negativo * 100) / contador

print('='* 10,'ANALISANDO','=' * 10)
print(f'MÉDIA ARITIMÉDICA dos valores lidos: {media}')
print(f'Números POSITIVOS: {positivo}')
print(f'Números NEGATIVOS: {negativo}')
print(f'Percentual de valores NEGATIVOS: {percentual_negativo:.0f}%')
print(f'Percentual de valores POSITIVOS: {percentual_posito:.0f}%')



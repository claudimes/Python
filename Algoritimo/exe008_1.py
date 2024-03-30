print('============== Exercicio 08 .1 ==============')
quantidade_quilometros = int(input('Digite a Quilometragem Rodada: '))
quantidade_combustivel = float(input('Agora informe a Litragem Consumida: '))
if quantidade_combustivel == 0:
    print('Media de consumo não pode ser calculada')
else:
    media_consumo = quantidade_quilometros / quantidade_combustivel
    print(f'A media do veiculo foi de: {media_consumo:.2f} kms por litro.')

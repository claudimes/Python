print ('================= Desafio 29 =================')
velocidade = int(input('Qual é a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print(f'Voce ultrapassou a velocidade permitida e Foi Multado em R$ {multa :.2f}.')
print('Tenha um Bom Dia! Dirija com Segurança.')

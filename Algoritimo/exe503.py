'''Faça uma função que recebe por parâmetro o raio de uma esfera e calcule o seu volume
(v = (4 x pi x R3)/3). '''
def calculo():
    volume = (4 * 3.14) * (raio ** 3) / 3
    return volume


raio = float(input('Qual o RAIO da Esfera (cm): '))
print(f'Uma Esfera com Raio de {raio} cm, tem o Volume de {calculo():.2f} cm.')


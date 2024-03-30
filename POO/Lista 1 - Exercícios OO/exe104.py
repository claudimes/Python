# Calcular a média de combustível gasto pelo usuário, sendo informado a quantidade de quilômetros
# rodados e a quantidade de combustível consumido.

class Usuario:
    def __init__(self):
        self.quantidade_de_quilômetros_rodados = 0
        self.quantidade_de_combustível_consumido = 0

    def media(self):
        return self.quantidade_de_quilômetros_rodados / self.quantidade_de_combustível_consumido


usuario1 = Usuario()
usuario1.quantidade_de_quilômetros_rodados = 180
usuario1.quantidade_de_combustível_consumido = 50

print('=-' * 5, 'Consumo Média Carro', '-=' * 5)
print(f'Média de combustível gasto: {usuario1.media():.2f} Km por Litro.')

# Efetuar a leitura do número de quilowatts consumidos e calcular o valor a ser pago de energia
# elétrica, sabendo-se que o valor a pagar por quilowatt é de 0,12. Apresentar o valor total a ser pago
# pelo usuário acrescido de 18% de ICMS.

class Consumidor:
    def __init__(self):
        self.numero_de_quilowatts = 0
        self.valor_quilowatts = 0.12
        self.porcentagem_icms = 18

    def consumo(self):
        self.consumo1 = (self.numero_de_quilowatts * self.valor_quilowatts)
        return self.consumo1

    def icms(self):
        return (self.consumo() * self.porcentagem_icms) / 100

    def FaturaFinal(self):
        return self.consumo() + self.icms()


consumidor1 = Consumidor()
consumidor1.numero_de_quilowatts = 200
print('=-' * 5, 'Energia Elétrica', '-=' * 5)
print(f'Valor da Conta de Energia: R$ {consumidor1.FaturaFinal():.2f}')


# Calcular o salário líquido do funcionário sabendo que este é constituído pelo salário bruto mais
# o valor das horas extras subtraindo 8% de INSS do total. Serão lidos nesse problema o salário bruto,
# o valor das horas extras e o número de horas extras. Apresentar ao final o salário líquido.

class Funcionario:

    def __init__(self):
        self.salario_bruto = 0
        self.valor_hora_extras = 0
        self.numero_das_horas_extras = 0

    def calculo_hora_extra(self):
        return self.numero_das_horas_extras * self.valor_hora_extras

    def inss(self):
        return (self.salario_bruto + self.calculo_hora_extra()) * 8 / 100

    def SalarioLiquido(self):
        return self.salario_bruto + self.calculo_hora_extra() - self.inss()


funcionario1 = Funcionario()
funcionario1.salario_bruto = 1000
funcionario1.numero_das_horas_extras = 10
funcionario1.valor_hora_extras = 20

print(f'Salário Líquido: R$ {funcionario1.SalarioLiquido():.2f}')

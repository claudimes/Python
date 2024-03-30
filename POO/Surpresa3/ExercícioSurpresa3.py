class Funcionario:

    def __init__(self):
        self.nome = ' '
        self.salario_bruto = 0
        self.total_acrecimos = 0
        self.total_descontos = 0

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getSalario_bruto(self):
        return self.salario_bruto

    def setSalario_bruto(self, salario_bruto):
        self.salario_bruto = salario_bruto

'''Continuar depois '''



       # def calcular_salario(self):
        #    return self.getsalario_bruto() + self.gettotal_acresimos() - self.gettotal_descontos()


funcionario1 = Funcionario()

funcionario1.setsalario_bruto(1000)
funcionario1.settotal_acresimos(100)
funcionario1.settotal_descontos(550)
print(f"O salario líquido do funcionario: {funcionario1.calcular_salario()}")


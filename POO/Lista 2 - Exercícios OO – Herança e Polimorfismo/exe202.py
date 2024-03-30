'''Crie um sistema de pagamento para uma empresa que possui três tipos de funcionários:
funcionários comuns, gerentes e diretores.
Cada funcionário recebe um salário mensal fixo,
mas os gerentes recebem um bônus adicional e os diretores têm uma participação nos lucros.
Crie um programa em Python que calcule e exiba o pagamento mensal para cada funcionário.

Crie uma classe abstrata chamada Funcionario com um campo salarioMensal e um
método abstrato calcularPagamento().

Crie três classes que herdam de Funcionario: FuncionarioComum, Gerente e Diretor.

Na classe FuncionarioComum, o pagamento mensal é o salário mensal fixo.

Na classe Gerente, o pagamento mensal é o salário mensal fixo mais um bônus fixo.

Na classe Diretor, o pagamento mensal é o salário mensal fixo mais uma participação nos
lucros que é calculada com base nos lucros da empresa.'''


class Funcionario:
    def __init__(self):
        self.salario_mensal_fixo = 0

    def set_salario_mensal_fixo(self, salario_mensal_fixo):
        self.salario_mensal_fixo = salario_mensal_fixo

    def get_salario_mensal_fixo(self):
        return self.salario_mensal_fixo

    def calcularPagamento(self):
        pass


class Funcionario_Comum(Funcionario):
    def __init__(self):
        Funcionario.__init__(self)

    def calcularPagamento(self):
        return self.get_salario_mensal_fixo()


class Gerente(Funcionario):
    def __init__(self):
        Funcionario.__init__(self)
        self.bonus_adicional = 0

    def set_bonus_adicional(self, bonus_adicional):
        self.bonus_adicional = bonus_adicional

    def get_bonus_adicional(self):
        return self.bonus_adicional

    def calcularPagamento(self):
        return self.get_salario_mensal_fixo() + self.get_bonus_adicional()


class Diretor(Funcionario):
    def __init__(self):
        Funcionario.__init__(self)
        self.participacao_lucros = 0

    def set_participacao_lucros(self, participacao_lucros):
        self.participacao_lucros = participacao_lucros

    def get_participacao_lucros(self):
        return self.participacao_lucros

    def calcularPagamento(self):
        return self.get_salario_mensal_fixo() + self.get_participacao_lucros()


funcionario_comum1 = Funcionario_Comum()
funcionario_comum1.set_salario_mensal_fixo(1000)

gerente1 = Gerente()
gerente1.set_salario_mensal_fixo(5000)
gerente1.set_bonus_adicional(1000)

diretor1 = Diretor()
diretor1.set_salario_mensal_fixo(10000)
diretor1.set_participacao_lucros(5000)

print('-=' * 5, "Funcionário Comum", '-=' * 5)
print(f'Salario Funcionario Comum R${funcionario_comum1.get_salario_mensal_fixo():.2f}')
print(f'Salario Final: R$ {funcionario_comum1.calcularPagamento():.2f}')

print('-=' * 5, "Gerente", '-=' * 5)
print(f'Salário Gerente: R$ {gerente1.get_salario_mensal_fixo():.2f}')
print(f"Bônus Adicional: R$ {gerente1.get_bonus_adicional():.2f}")
print(f'Total a Receber: R$ {gerente1.calcularPagamento():.2f}')

print('-=' * 5, "Diretor", '-=' * 5)
print(f'Salário Diretor: R$ {diretor1.get_salario_mensal_fixo():.2f}')
print(f'Participação dos Lucros: R$ {diretor1.get_participacao_lucros():.2f}')
print(f'Total a Receber: R$ {diretor1.calcularPagamento():.2f}')

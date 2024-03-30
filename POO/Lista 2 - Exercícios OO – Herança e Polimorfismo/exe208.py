"""Crie um programa Python para um sistema de gerenciamento de veículos que possui diferentes tipos de
veículos, como carros, motos e bicicletas, cada um com suas próprias características e métodos de cálculo de custo.
Crie classes para representar os diferentes tipos de veículos e implemente esses métodos.

Crie uma classe abstrata chamada Veiculo com campos para marca, modelo e preço base.
Inclua um método abstrato calcularCusto().

Crie três classes que herdam de Veiculo: Carro, Moto e Bicicleta.

Na classe Carro, o método calcularCusto() calcula o custo com base no preço base
multiplicado por um fator fixo para carros.

Na classe Moto, o método calcularCusto() calcula o custo com base no preço base
multiplicado por um fator fixo para motos.

Na classe Bicicleta, o método calcularCusto() calcula o custo com base no preço base
multiplicado por um fator fixo para bicicletas."""


class Veiculo:
    def __init__(self):
        self.marca = " "
        self.modelo = " "
        self.preco_base = 0

    def set_marca(self, marca):
        self.marca = marca

    def get_marca(self):
        return self.marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo

    def set_preco_base(self, preco_base):
        self.preco_base = preco_base

    def get_preco_base(self):
        return self.preco_base

    def calcularCusto(self):
        pass


class Carro(Veiculo):
    def __init__(self):
        Veiculo.__init__(self)
        self.fator_fixo = 10

    def calcularCusto(self):
        return self.fator_fixo * self.get_preco_base()


class Moto(Veiculo):
    def __init__(self):
        Veiculo.__init__(self)
        self.fator_fixo = 5

    def calcularCusto(self):
        return self.fator_fixo * self.get_preco_base()


class Bicicleta(Veiculo):
    def __init__(self):
        Veiculo.__init__(self)
        self.fator_fixo = 3

    def calcularCusto(self):
        return self.fator_fixo * self.get_preco_base()


print("Carro")
carro = Carro()
carro.set_preco_base(5)
print(carro.calcularCusto())

print('Moto')
moto = Moto()
moto.set_preco_base(5)
print(moto.calcularCusto())

print('Bicicleta')
bicicleta = Bicicleta()
bicicleta.set_preco_base(5)
print(bicicleta.calcularCusto())

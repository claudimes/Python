'''Considere uma hierarquia de formas geométricas, incluindo círculos e retângulos.
Cada forma deve ter um método calcularArea() que calcula a área da forma e um método
calcularPerimetro() que calcula o perímetro da forma.
Você deve usar polimorfismo para implementar esses métodos nas classes específicas de círculo e retângulo.

Crie uma classe abstrata chamada FormaGeometrica com os métodos abstratos calcularArea() e calcularPerimetro().

Crie uma classe Circulo que herda de FormaGeometrica e inclua campos para o raio.

Implemente os métodos calcularArea() e calcularPerimetro() para o círculo.

Crie uma classe Retangulo que herda de FormaGeometrica e inclua campos para a largura e altura.
Implemente os métodos calcularArea() e calcularPerimetro() para o retângulo.
'''

class FormaGeometrica:
    pi = 3.14
    def __init__(self):
        pass

    def calcularArea(self):
        pass

    def calcularPerimetro(self):
        pass

class Circulo(FormaGeometrica):
    def __init__(self):
        FormaGeometrica.__init__(self)
        self.raio = 0

    def set_raio(self, raio):
        self.raio = raio

    def get_raio(self):
        return self.raio

    def calcularArea(self):
        return (Circulo.pi * (self.get_raio() **2))

    def calcularPerimetro(self):
        return (2 *(Circulo.pi * self.get_raio()))

class Retangulo(FormaGeometrica):
    def __init__(self):
        FormaGeometrica.__init__(self)
        self.largura = 0
        self.altura = 0

    def set_largura(self, largura):
        self.largura = largura

    def get_largura(self):
        return self.largura

    def set_altura(self, altura):
        self.altura = altura

    def get_altura(self):
        return self.altura

    def calcularArea(self):
        return (self.get_altura() * self.get_largura())

    def calcularPerimetro(self):
        return (2 * (self.get_altura() + self.get_largura()))

circulo1 = Circulo()
circulo1.set_raio(5)

retangulo1 = Retangulo()
retangulo1.set_largura(10)
retangulo1.set_altura(5)

print('-=' * 5, 'Círculo', '-=' * 5)
print(f'Calcular Área: {circulo1.calcularArea()} cm²')
print(f"Calcular Perímetro: {circulo1.calcularPerimetro():.4f}")

print('-=' * 5, 'Retângulo', '-=' * 5)
print(f'Calcular Área: {retangulo1.calcularArea()} cm²')
print(f"Calcular Perímetro: {retangulo1.calcularPerimetro()} cm")


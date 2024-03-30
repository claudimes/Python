"""Crie um programa Python para um sistema de reservas de passagens em uma companhia aérea.
O sistema deve lidar com diferentes tipos de voos, como voos domésticos e voos internacionais,
cada um com suas próprias regras de precificação.
Crie classes para representar os diferentes tipos de voos e implemente um método de cálculo de preço.

Crie uma classe abstrata chamada Voo com campos para origem, destino e data do voo.
Inclua um método abstrato calcularPreco().

Crie duas classes que herdam de Voo: VooDomestico e VooInternacional.

Na classe VooDomestico, o preço base é calculado com base na distância entre a origem
e o destino multiplicada por um .

Na classe VooInternacional, o preço base é calculado com base na distância entre a origem e o destino
multiplicada por um fator de preço específico para voos internacionais,
além de uma taxa de conversão de moeda, se aplicável."""


class Voo:
    def __init__(self):
        self.origem = " "
        self.destino = " "
        self.data_do_voo = " "

    def set_origem(self, origem):
        self.origem = origem

    def get_origem(self):
        return self.origem

    def set_destino(self, destino):
        self.destino = destino

    def get_destino(self):
        return self.destino

    def set_data_do_voo(self, data_do_voo):
        self.data_do_voo = data_do_voo

    def get_data_do_voo(self):
        return self.data_do_voo

    def calcularPreco(self):
        pass


class VooDomestico(Voo):
    def __init__(self):
        Voo.__init__(self)
        self.distancia = 0
        self.fator_voo_dom = 0

    def set_distancia(self, distancia):
        self.distancia = distancia

    def get_distancia(self):
        return self.distancia

    def set_fator_voo_dom(self, fator_voo_dom):
        self.fator_voo_dom = fator_voo_dom

    def get_fator_voo_dom(self):
        return self.fator_voo_dom

    def calcularPreco(self):
        return self.get_fator_voo_dom() * self.get_distancia()


class VooInternacional(Voo):
    def __init__(self):
        Voo.__init__(self)
        self.distancia = 0
        self.fator_voo_int = 0
        self.taxa_conversao_moeda = 0

    def set_distancia(self, distancia):
        self.distancia = distancia

    def get_distancia(self):
        return self.distancia

    def set_fator_voo_int(self, fator_voo_int):
        self.fator_voo_int = fator_voo_int

    def get_fator_voo_int(self):
        return self.fator_voo_int

    def set_taxa_conversao_moeda(self, taxa_conversao_moeda):
        self.taxa_conversao_moeda = taxa_conversao_moeda

    def get_taxa_conversao_moeda(self):
        return self.taxa_conversao_moeda

    def calcularPreco(self):
        if self.get_taxa_conversao_moeda() != 0:
            return (self.get_taxa_conversao_moeda() * self.get_fator_voo_int()) * self.get_distancia()
        else:
            return self.get_fator_voo_int() * self.get_distancia()


voo_domestico1 = VooDomestico()
voo_domestico1.set_data_do_voo("15/12/2023")
voo_domestico1.set_origem('Juiz de Fora')
voo_domestico1.set_destino('Fortaleza')
voo_domestico1.set_distancia(500)
voo_domestico1.set_fator_voo_dom(5)

voo_internacional1 = VooInternacional()
voo_internacional1.set_data_do_voo("04/05/2024")
voo_internacional1.set_origem('Juiz de Fora')
voo_internacional1.set_destino('Nova Iork')
voo_internacional1.set_distancia(7631)
voo_internacional1.set_fator_voo_int(5)
voo_internacional1.set_taxa_conversao_moeda(5)

print('-=' * 5, "Azul Linhas Aéreas - Vôo Doméstico", '-=' * 5)
print(f'Data Voo: {voo_domestico1.get_data_do_voo()}')
print(f'Origem: {voo_domestico1.get_origem()}')
print(f'Destino: {voo_domestico1.get_destino()}')
print(f'Preço á Pagar: R$ {voo_domestico1.calcularPreco():.2f}')

print('-=' * 5, "Azul Linhas Aéreas - Vôo Internacional", '-=' * 5)
print(f'Data Voo: {voo_internacional1.get_data_do_voo()}')
print(f'Origem: {voo_internacional1.get_origem()}')
print(f'Destino: {voo_internacional1.get_destino()}')
print(f'Preço á Pagar: R$ {voo_internacional1.calcularPreco():.2f}')

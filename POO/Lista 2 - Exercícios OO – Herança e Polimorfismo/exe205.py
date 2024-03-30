"""Crie um programa Python para um sistema de gerenciamento de produtos em uma loja.
O sistema deve lidar com diferentes tipos de produtos, como eletrônicos, roupas e alimentos,
cada um com suas próprias características e métodos de cálculo de preço.
Crie classes para representar os diferentes tipos de produtos e implemente métodos para calcular o
preço total com base nas quantidades compradas.

Crie uma classe abstrata chamada Produto com campos para nome, preço unitário e quantidade em estoque.
Inclua um método abstrato calcularPreco().

Crie três classes que herdam de Produto: ProdutoEletronico, ProdutoRoupa e ProdutoAlimento.

Na classe ProdutoEletronico, o preço unitário é o preço de varejo e o cálculo do preço total
leva em consideração a quantidade e um possível desconto.

Na classe ProdutoRoupa, o preço unitário é o preço de etiqueta e o cálculo do preço total leva em consideração
a quantidade e um possível desconto.

Na classe ProdutoAlimento, o preço unitário é o preço por quilo e o cálculo do preço total leva
em consideração a quantidade em quilos."""


class Produto:
    def __init__(self):
        self.nome = " "
        self.preco_unitario = 0
        self.quantidade_em_estoque = 0
        self.quantidade = 0
        self.desconto = 0

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_preco_unitario(self, preco_unitario):
        self.preco_unitario = preco_unitario

    def get_preco_unitario(self):
        return self.preco_unitario

    def set_quantidade_em_estoque(self, quantidade_em_estoque):
        self.quantidade_em_estoque = quantidade_em_estoque

    def get_quantidade_em_estoque(self):
        return self.quantidade_em_estoque

    def set_quantidade(self, quantidade):
        self.quantidade = quantidade

    def get_quantidade(self):
        return self.quantidade

    def set_desconto(self, desconto):
        self.desconto = desconto

    def get_desconto(self):
        return self.desconto

    def calcularPreco(self):
        pass


class ProdutoEletronico(Produto):
    def __init__(self):
        Produto.__init__(self)

    def calcularPreco(self):
        if self.get_desconto() != 0:
            valor_desconto = (self.get_quantidade() * self.get_preco_unitario()) * self.get_desconto() / 100
            return ((self.get_quantidade() * self.get_preco_unitario()) - valor_desconto)
        else:
            return (self.get_quantidade() * self.get_preco_unitario())


class ProdutoRoupa(Produto):
    def __init__(self):
        Produto.__init__(self)

    def calcularPreco(self):
        if self.get_desconto() != 0:
            valor_desconto = (self.get_quantidade() * self.get_preco_unitario()) * self.get_desconto() / 100
            return ((self.get_quantidade() * self.get_preco_unitario()) - valor_desconto)
        else:
            return (self.get_quantidade() * self.get_preco_unitario())


class ProdutoAlimento(Produto):
    def __init__(self):
        Produto.__init__(self)
        self.quant_por_quilo = 0

    def set_quant_por_quilo(self, quant_por_quilo):
        self.quant_por_quilo = quant_por_quilo

    def get_quant_por_quilo(self):
        return self.quant_por_quilo

    def calcularPreco(self):
        return (self.get_preco_unitario() * self.get_quant_por_quilo())


produto_eletronico = ProdutoEletronico()
produto_eletronico.set_nome("Nootebook")
produto_eletronico.set_preco_unitario(3500)
produto_eletronico.set_quantidade_em_estoque(10)
produto_eletronico.set_quantidade(2)
produto_eletronico.set_desconto(10)

produto_roupa = ProdutoRoupa()
produto_roupa.set_nome("Calça Jeans")
produto_roupa.set_preco_unitario(500)
produto_roupa.set_quantidade_em_estoque(10)
produto_roupa.set_quantidade(3)
produto_roupa.set_desconto(5)

produto_alimento = ProdutoAlimento()
produto_alimento.set_nome("Salmão")
produto_alimento.set_preco_unitario(100)
produto_alimento.set_quant_por_quilo(5)

print('-=' * 5, "Magazine Gomes - Produto Eletrônico", '-=' * 5)
if produto_eletronico.get_quantidade() > produto_eletronico.get_quantidade_em_estoque():
    print("Venda não permitida. Quantidade acima do Estoque Disponivel!")
else:
    print(f'Produto: {produto_eletronico.get_nome()}')
    print(f'Preço Unitário: R$ {produto_eletronico.get_preco_unitario():.2f}')
    print(f'Quantidade em Estoque: {produto_eletronico.get_quantidade_em_estoque()}')
    print(f'Quantidade: {produto_eletronico.get_quantidade()}')
    print(f'Desconto: {produto_eletronico.get_desconto()} %')
    print(f'Total a Pagar: R$ {produto_eletronico.calcularPreco():.2f}')

print('-=' * 5, "Magazine Gomes - Produto Eletrônico", '-=' * 5)
if produto_roupa.get_quantidade() > produto_roupa.get_quantidade_em_estoque():
    print("Venda não permitida. Quantidade acima do Estoque Disponivel!")
else:
    print(f'Produto: {produto_roupa.get_nome()}')
    print(f'Preço Unitário: R$ {produto_roupa.get_preco_unitario():.2f}')
    print(f'Quantidade em Estoque: {produto_roupa.get_quantidade_em_estoque()}')
    print(f'Quantidade: {produto_roupa.get_quantidade()}')
    print(f'Desconto: {produto_roupa.get_desconto()} %')
    print(f'Total a Pagar: R$ {produto_roupa.calcularPreco():.2f}')

print('-=' * 5, "Magazine Gomes - Produto Eletrônico", '-=' * 5)
print(f'Produto: {produto_alimento.get_nome()}')
print(f'Preço Unitário: R$ {produto_alimento.get_preco_unitario():.2f}')
print(f'Quant. Kilos: {produto_alimento.get_quant_por_quilo()}')
print(f'Total a Pagar: R$ {produto_alimento.calcularPreco():.2f}')

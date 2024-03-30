"""Crie um programa Python para um sistema de pedidos em uma loja online.
O sistema deve lidar com diferentes tipos de produtos, como eletrônicos, roupas e livros.
Cada tipo de produto tem um preço base e pode ter descontos específicos.

Crie classes para representar os diferentes tipos de produtos e implemente um método de cálculo de preço com desconto.

Crie uma classe abstrata chamada Produto com campos para nome e preço base.
Inclua um método abstrato calcularPreco().

Crie três classes que herdam de Produto: ProdutoEletronico, ProdutoRoupa e ProdutoLivro.

Na classe ProdutoEletronico, o preço base é o preço de varejo e pode ter um desconto de 10%.

Na classe ProdutoRoupa, o preço base é o preço de etiqueta e pode ter um desconto de 20%.

Na classe ProdutoLivro, o preço base é o preço de capa e pode ter um desconto de 5%."""


class Produto:
    def __init__(self):
        self.nome = " "
        self.preco_base = 0
        self.desconto = 0

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_preco_base(self, preco_base):
        self.preco_base = preco_base

    def get_preco_base(self):
        return self.preco_base

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
            return self.get_preco_base() - (self.get_preco_base() * self.get_desconto() / 100)
        else:
            return self.get_preco_base()


class ProdutoRoupa(Produto):
    def __init__(self):
        Produto.__init__(self)

    def calcularPreco(self):
        if self.get_desconto() != 0:
            return self.get_preco_base() - (self.get_preco_base() * self.get_desconto() / 100)
        else:
            return self.get_preco_base()


class ProdutoLivro(Produto):
    def __init__(self):
        Produto.__init__(self)

    def calcularPreco(self):
        if self.get_desconto() != 0:
            return self.get_preco_base() - (self.get_preco_base() * self.get_desconto() / 100)
        else:
            return self.get_preco_base()


produto_eletronico1 = ProdutoEletronico()
produto_eletronico1.set_nome('Calculadora Ciêntifica')
produto_eletronico1.set_preco_base(100)
produto_eletronico1.set_desconto(10)

produto_roupa1 = ProdutoRoupa()
produto_roupa1.set_nome('Camisa Polo Vermelha')
produto_roupa1.set_preco_base(399)
produto_roupa1.set_desconto(20)

produto_livro1 = ProdutoLivro()
produto_livro1.set_nome('Use a Cabeça Análise e Projeto Orientado a Objetos')
produto_livro1.set_preco_base(300)
produto_livro1.set_desconto(5)

print('-=' * 5, "Produto Eletrônico", '-=' * 5)
print(f'Produto: {produto_eletronico1.get_nome()}')
print(f"Valor: R$ {produto_eletronico1.get_preco_base():.2f}")
print(f'Desconto: {produto_eletronico1.get_desconto()} %')
print(f'Total com Desconto: R$ {produto_eletronico1.calcularPreco():.2f}')

print('-=' * 5, "Produto Roupa", '-=' * 5)
print(f'Produto: {produto_roupa1.get_nome()}')
print(f"Valor: R$ {produto_roupa1.get_preco_base():.2f}")
print(f'Desconto: {produto_roupa1.get_desconto()} %')
print(f'Total com Desconto: R$ {produto_roupa1.calcularPreco():.2f}')

print('-=' * 5, "Produto Livro", '-=' * 5)
print(f'Produto: {produto_livro1.get_nome()}')
print(f"Valor: R$ {produto_livro1.get_preco_base():.2f}")
print(f'Desconto: {produto_livro1.get_desconto()} %')
print(f'Total com Desconto: R$ {produto_livro1.calcularPreco():.2f}')

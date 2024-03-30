'''Crie um programa Python para um sistema de biblioteca que gerencia diferentes tipos de materiais,
como livros, revistas e filmes. Cada tipo de material tem seu próprio método de cálculo de empréstimo e
datas de devolução. Crie classes para representar os diferentes tipos de materiais e implemente esses métodos.

Crie uma classe abstrata chamada MaterialBiblioteca com campos para título e data de publicação.
Inclua um método abstrato calcularDataDevolucao().

Crie três classes que herdam de MaterialBiblioteca: Livro, Revista e Filme.

Na classe Livro, o método calcularDataDevolucao() calcula a data de devolução baseada
em um prazo fixo, por exemplo, 15 dias após o empréstimo.

Na classe Revista, o método calcularDataDevolucao() calcula a data de devolução
baseada em um prazo fixo diferente, por exemplo, 7 dias após o empréstimo.

Na classe Filme, o método calcularDataDevolucao() calcula a data de devolução baseada
em um prazo fixo, por exemplo, 5 dias após o empréstimo.'''

import datetime


class MaterialBiblioteca:
    def __init__(self):
        self.titulo = " "
        self.data_de_publicacao = " "
        self.data_emprestimo = " "

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo

    def set_data_de_publicacao(self, data_de_publicacao):
        self.data_de_publicacao = data_de_publicacao

    def get_data_de_publicacao(self):
        return self.data_de_publicacao

    def calcularDataDevolucao(self):
        data_emprestimo = datetime.date.fromisoformat(self.data_emprestimo)  # Convertendo Data Srt para date
        data_atual = datetime.datetime.today().date()
        dias_emprestado = (data_atual - data_emprestimo).days  # Calculando a quantidade de dias emprestado
        if dias_emprestado <= self.prazo_fixo:
            return "Em Dia!"
        else:
            return "Em Atraso!"


# Na classe Livro, o método calcularDataDevolucao() calcula a data de devolução baseada
# em um prazo fixo, por exemplo, 15 dias após o empréstimo.
class Livro(MaterialBiblioteca):
    def __init__(self):
        MaterialBiblioteca.__init__(self)
        self.prazo_fixo = 15


# Na classe Revista, o método calcularDataDevolucao() calcula a data de devolução
# baseada em um prazo fixo diferente, por exemplo, 7 dias após o empréstimo.
class Revista(MaterialBiblioteca):
    def __init__(self):
        MaterialBiblioteca.__init__(self)
        self.prazo_fixo = 7


# Na classe Filme, o método calcularDataDevolucao() calcula a data de devolução baseada
# em um prazo fixo, por exemplo, 5 dias após o empréstimo.
class Filme(MaterialBiblioteca):
    def __init__(self):
        MaterialBiblioteca.__init__(self)
        self.prazo_fixo = 5


print('Livro com 15 Dias')
livro = Livro()
livro.data_emprestimo = "2023-09-24"
print(livro.calcularDataDevolucao())

print('Revista com 7 Dias')
revista = Revista()
revista.data_emprestimo = "2023-10-02"
print(revista.calcularDataDevolucao())

print('Filme com 5 Dias')
filme = Filme()
filme.data_emprestimo = "2023-10-04"
print(filme.calcularDataDevolucao())

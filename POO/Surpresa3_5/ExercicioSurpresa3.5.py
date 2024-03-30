class Pessoa:

    def __init__(self):
        self.nome = " "


class Aluno(Pessoa):

    def __init__(self):
        Pessoa.__init__()
        self.matricula = 0
        self.nota = 0
        self.nota2 = 0

class AlunoEnsinoMedio(Aluno):

    def __init__(self):
        Aluno.__init__()

    def calcular_media(self):
        if (self.nota + self.nota2 / 2) < 6:
            return "Reprovado"
        else:
            "Aprovado"

class AlunoEnsinoSuperior(Aluno):
    def __init__(self):
        Aluno.__init__(self)


    def calcular_media_superior(self):
        if(self.nota + self.nota2 / 2) < 7:
            return "Reprovado"
        else:
            "Aprovado"

alunoensinomedio1 = AlunoEnsinoMedio()
alunoensinomedio1.nome = "João"
alunoensinomedio1.matricula = 2555
alunoensinomedio1.nota = 5
alunoensinomedio1.nota2 = 5
print(alunoensinomedio1.calcular_media())


class Empresa:
    def __init__(self, nome_empresa):
        self.grupo = None
        self.diretor = None

    def setGrupo(self, grupo):
        self.grupo = grupo

    def getGrupo(self):
        return self.grupo

    def setDiretor(self, diretor):
        self.diretor = diretor

    def getDiretor(self):
        return self.diretor

class Escola:
    def __init__(self):
        self.diretor = None


    def setDiretor(self, diretor):
        self.diretor = diretor

    def getDiretor(self):
        return self.diretor

    def getEscolaridadeDiretor(self):
        if self.diretor == None:
            return 'Escola sem Diretor'
        else:
            return self.diretor.getEscolaridadeProfessor()

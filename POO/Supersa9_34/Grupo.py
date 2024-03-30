class Grupo:
    def __init__(self):
        self.presidente = None
        self.sede = None

    def setPresidente(self, presidente):
        self.presidente = presidente

    def getPresidente(self):
        return self.presidente

    def setSede(self, sede):
        self.sede = sede

    def getSede(self):
        return self.sede

    def getEscolaridadePresidenteGrupo(self):
        if self.presidente == None:
            return 'Grupo sem Presidente'
        else:
            return self.presidente.escolaridade.getDescricao()

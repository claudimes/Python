class Departamento:
    def __init__(self):
        self.empresa = None
        self.chefia = None

    def setEmpresa(self, empresa):
        self.empresa = empresa

    def getEmpresa(self):
        return self.empresa

    def setChefia(self, chefia):
        self.chefia = chefia

    def getChefia(self):
        return self.chefia

    def getEscolaridadeChefeDepartamento(self):
        if self.chefia == None:
            return 'Sem Chefia'
        else:
            return self.chefia.escolaridade.getDescricao()

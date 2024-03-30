class Filial:
    def __init__(self):
        self.cidade = None
        self.empresa = None

    def setCidade(self, cidade):
        self.cidade = cidade

    def getCidade(self):
        return self.cidade

    def setEmpresa(self, empresa):
        self.empresa = empresa

    def getEmpresa(self):
        return self.empresa


    def getNomeDiretorEmpresaFilial(self):
        return self.empresa.diretor.getNome()

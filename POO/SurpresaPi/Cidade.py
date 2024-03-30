class Cidade:
    def __init__(self, cidade):
        self.cidade = cidade
        self.estado = None

    def setCidade(self, cidade):
        self.cidade = cidade

    def getCidade(self):
        return self.cidade

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

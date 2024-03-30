class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.cordenador = None
        self.tipo_ensino = None
        self.escola = None

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setCordenador(self, cordenador):
        self.cordenador = cordenador

    def getCordenador(self):
        return self.cordenador

    def setTipo_Ensino(self, tipo_ensino):
        self.tipo_ensino = tipo_ensino

    def getTipo_Ensino(self):
        return self.tipo_ensino

    def setEscola(self, escola):
        self.escola = escola

    def getEscola(self):
        return self.escola

    def getEscolaridadeCordenador(self):
        if self.cordenador == None:
            return 'Curso sem Cordenador'
        else:
            return self.cordenador.getEscolaridadeProfessor()

class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        self.escolaridade = None
        self.alocacao = None
        self.coordenador = None
        self.departamento = None

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade

    def getEscolaridade(self):
        return self.escolaridade

    def setAlocacao(self, alocacao):
        self.alocacao = alocacao

    def getAlocacao(self):
        return self.alocacao

    def setCoordenador(self, coordenador):
        self.coordenador = coordenador

    def getCoordenador(self):
        return self.coordenador

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def getDepartamento(self):
        return self.departamento

    def getPaisAlocacaoFuncionario(self):
        if self.alocacao is None:
            return 'Sem Funcionário alocado.'
        else:
            return self.alocacao.empresa.grupo.sede.getNome_Pais()

    def getEstadoFilialFuncionarioCoordenador(self):
        if self.coordenador == None:
            return 'Sem Coordenador'
        else:
            return self.coordenador.cidade.estado.getUF()


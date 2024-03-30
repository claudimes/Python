class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.escolaridade = None
        self.naturalidade = None
        self.cidade = None
        self.curso = None

    def setNome(self, nome):
        self.nome = nome


    def getNome(self):
        return self.nome


    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade


    def getEscolaridade(self):
        return self.escolaridade


    def setNaturalidade(self, naturalidade):
        self.naturalidade = naturalidade


    def getNaturalidade(self):
        return self.naturalidade


    def setCidade(self, cidade):
        self.cidade = cidade


    def getCidade(self):
        return self.cidade


    def setCurso(self, curso):
        self.curso = curso


    def getCurso(self):
        return self.curso


    def getEscolaridadeProfessor(self):
        if self.escolaridade == None:
            return 'Professor sem Escolaridade'
        else:
            return self.escolaridade.getDescricao()


    def getCidadeNascimentoProfessor(self):
        if self.naturalidade == None:
            return 'Professor sem Cidade Cadastrada'
        else:
            return self.naturalidade.getCidade()


    def getTipoEnsinoProfessorLeciona(self):
        if (self.curso == None) or (self.curso.getTipo_Ensino() == None):
            return 'Professor sem Tipo de Ensino/Curso'
        else:
            return self.curso.tipo_ensino.getEnsino()


    def getDiretordeProfessor(self):
        if (self.curso == None)  or (self.curso.escola.getDiretor()) == None:
            return 'Professor sem Diretor'
        else:
            return self.curso.escola.diretor.getNome()


    def getCordenadorProfessor(self):
        if (self.curso == None) or (self.curso.getCordenador() == None):
            return 'Professor sem Cordenador'
        else:
            return self.curso.cordenador.getNome()


    def getCordenadorCursoAluno(self):
        if (self.curso == None) or (self.curso.getCordenador() == None):
            return 'Aluno sem Curso/Cordenador'
        else:
            return self.curso.cordenador.getNome()

    def getNaturalidadeAluno(self):
        if self.naturalidade == None:
            return 'Aluno sem Naturalidade'
        else:
            return self.naturalidade.estado.getUf()

    def getEstadoAlunoEstuda(self):
        if (self.cidade == None) or (self.cidade.getEstado() == None):
            return f'Estado/Cidade não cadastrado para o aluno {self.nome}'
        else:
            return self.cidade.estado.getUf()


from SurpresaPi.Aluno import Aluno
from SurpresaPi.Estado import Estado
from SurpresaPi.Cidade import Cidade

print('F) Qual o Estado em que o Aluno Estuda?')

estado = Estado('SP')

cidade = Cidade('Guaratingueta')
cidade.setEstado(estado)

aluno = Aluno('Lara')
aluno.setCidade(cidade)

print(aluno.getEstadoAlunoEstuda())



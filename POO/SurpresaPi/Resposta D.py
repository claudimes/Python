from SurpresaPi.Aluno import Aluno
from SurpresaPi.Estado import Estado
from SurpresaPi.Cidade import Cidade

print('D) Qual estado de naturalidade de um aluno?')

estado = Estado('MG')

cidade = Cidade('Juiz de Fora')
cidade.setEstado(estado)

aluno = Aluno('Claudio')
aluno.setNaturalidade(cidade)

print(aluno.getNaturalidadeAluno())

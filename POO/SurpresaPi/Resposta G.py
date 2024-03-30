from SurpresaPi.Curso import Curso
from SurpresaPi.Professor import Professor
from SurpresaPi.TipodeEnsino import TipodeEnsino

print('G) Qual o Tipo de Ensino(ensino Fundamental, medio ou superior) em que um professor foi contrato para lecionar?')

tipo_ensino = TipodeEnsino('Graduação')

curso = Curso('Ciencia da Computação')
curso.setTipo_Ensino(tipo_ensino)

professor = Professor('Davis')
professor.setCurso(curso)

print(professor.getTipoEnsinoProfessorLeciona())





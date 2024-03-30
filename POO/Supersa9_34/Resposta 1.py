from Escolaridade import Escolaridade
from Funcionario import Funcionario
from Grupo import Grupo

print('Qual a escolaridade do presidente de um grupo?')

escolaridade = Escolaridade('Doutorado')
funcionario = Funcionario('Claudio')
presidente = Grupo()
funcionario.setEscolaridade(escolaridade)
presidente.setPresidente(funcionario)

print(presidente.getEscolaridadePresidenteGrupo())




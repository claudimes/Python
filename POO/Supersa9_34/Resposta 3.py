from Cidade import Cidade
from Estado import Estado
from Filial import Filial
from Funcionario import Funcionario

print('Qual Estado da filial que um funcionario coordena?')

estado = Estado('RJ')
cidade = Cidade()
filial = Filial()
coordenador = Funcionario('Antônio')
cidade.setEstado(estado)
filial.setCidade(cidade)
coordenador.setCoordenador(filial)

print(coordenador.getEstadoFilialFuncionarioCoordenador())











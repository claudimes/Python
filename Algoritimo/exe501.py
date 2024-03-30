'''Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e
retorna essa idade expressa em dias'''

def idade():
    resultado = dias + (meses * 30) + (anos * 365)
    return resultado


anos = int(input('Quantos ANOS: '))
meses = int(input('Quantos MESES: '))
dias = int(input('Quantos DIAS: '))

print(f'Sua IDADE convertida em dias é: {idade()}')




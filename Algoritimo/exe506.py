'''Escrever uma função calcularQuociente(dividendo, divisor),que retorna a divisão inteira
(sem casas decimais) de dividendo por divisor e outra funçãocalcularResto(dividendo, divisor)
 que retorna o resto.'''

def calcularQuociente(dividendo, divisor):
    inteira = dividendo // divisor
    return inteira

def calcularResto (dividendo, divisor):
    resto = dividendo % divisor
    return resto

dividendo = int(input('Digite o Dividendo: '))
divisor = int(input('Digite o Divisor: '))
print(f'A Divivisão INTEIRA entre {dividendo}/{divisor} =',calcularQuociente(dividendo, divisor))
print(f'O RESTO da divisão entre {dividendo}/{divisor} =',calcularResto(dividendo, divisor))






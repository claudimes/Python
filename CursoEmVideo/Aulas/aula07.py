#nome = input('Qual é os seu Nome: ')
#print('Prazer em te conhecer {:=^20}'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 # Divisão Inteira
e = n1 ** n2 # Potencia
print('A soma é {}, \n o produto é {} e \n a divisão é {:.2f}'.format(s, m, d), end=' ')
print('Divisão inteira é {} e potencia {}'.format(di, e))
# {:.2f} duas casas decimais flutuantes
# Para não quebra a linha de um print para outro use o end= ' '
# Para quebrae a linha no meio do print use o \n
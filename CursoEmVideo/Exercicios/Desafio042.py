print('================= Desafio 42 =================')
print(' ')
print('-=-' * 20)
print('Analisador de Triangulos')
print('-=-' * 20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo!')
    if r1 == r2 and r1 == r3:
        print('Todos os lados Iguais. Triangulo Equilatero!')
    else:
        if r1 == r2 or r1 == r3 or r2 == r3:
            print('Dois lados Iguais. Triangulo Isósceles!')
        else:
            print('Todos os lados Diferentes. Triangulo Escaleno!')
else:
    print('Os segmentos acima NAO PODEM FORMAR um triangulo!')
#3.	Faça uma função recursiva para exibir os números compreendidos entre a e b,
# sendo a e b parâmetros da função.

def impimir(a, b):
    if a <= b:
        if b != a:
            impimir(a, b - 1)
        print(b,'->', end=" ")
    else:
        if a != b:
            impimir(b, a - 1)
        print(a,'->', end=" ")

a = int(input('Digite o 1º Número: '))
b = int(input('Digite o 2º Número: '))
impimir(a, b)
print('FIM')

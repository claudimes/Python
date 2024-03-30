#4.	Pesquise a sequência de Fibonacci e faça uma função recursiva para exibir seus n primeiros
# termos, sendo n um parâmetro da função.

def fibonacci(n):
    if n == 0:
        return 0
    return n + fibonacci(n - 1)

n = 5
print(fibonacci(n))

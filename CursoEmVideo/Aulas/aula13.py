n = 1
numero_perfeito = 0
while numero_perfeito < 3:
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma +=  i
    if soma == n:
        numero_perfeito += 1
        print(f'Numero {n} é perfeiro')
    n += 1


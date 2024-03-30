numero_perfeito = 0
numero = 1

while numero_perfeito < 3:
    soma = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma = soma + i
    if soma == numero:
        print(numero, "é um número perfeito.")
        numero_perfeito = numero_perfeito + 1
    numero = numero + 1


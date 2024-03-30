valor = 1
soma = 0
contador = 0

while valor > 0:
    valor = int(input('Digite um numero: '))
    if valor > 0:
        soma = soma + valor
        contador = contador + 1
media = soma / contador
print(f"A média aritmética dos valores informados é {media:.0f}. ")


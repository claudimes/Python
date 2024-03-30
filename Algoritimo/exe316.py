n = int(input("Digite um número inteiro e positivo: "))
soma = 0

for i in range(1, n+1):
    soma = soma + 1/i
    print(soma)

print("A soma da série é:", soma)

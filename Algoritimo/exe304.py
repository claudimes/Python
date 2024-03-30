salario = 1
contador = 0
filhos = 0
soma_salario = 0
maior_salario = 0
contador_100 = 0
percentual_salario = 0
while salario > 0:
    salario = float(input('Digite seu Salario: R$ '))
    if salario > 0:
        n_filhos = int(input('Quantos Filhos? '))
        soma_salario = soma_salario + salario
        contador = contador + 1
        filhos = filhos + n_filhos

        if salario > maior_salario:
            maior_salario = salario
        if salario <= 100:
            contador_100 = contador_100 + 1
            percentual_salario = (contador_100 * 100) / contador

media_salario = soma_salario / contador
media_filhos = filhos / contador

print(f"Maior Salario R$: {maior_salario:.2f}")
print(f"Média do salário da população R$: {media_salario:.2f}")
print(f"Média do número de filhos: {media_filhos:.0f}")
print(f"Percentual de pessoas com salário até R$ 100,00: {percentual_salario:.0f}%")

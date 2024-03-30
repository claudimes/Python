print ('================= Desafio 33 =================')
n1 = int(input('Digite o Primeiro Numero: '))
n2 = int(input('Digite o Segundo Numero: '))
n3 = int(input('Digite o Terceiro numero: '))
#Verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verificando o Maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor valor digitado foi {menor}.')
print(f'O maior valor digitado foi {maior}.')

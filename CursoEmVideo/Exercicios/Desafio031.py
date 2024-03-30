print ('================= Desafio 31 =================')
distancia = float(input('Qual a distancia da sua viagem? '))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print(f' Para uma viagem de {distancia} km, voce vai pagar R$ {passagem :.2f}.')

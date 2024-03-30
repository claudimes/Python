print ('================= Desafio 18 =================')
import math
angulo = float(input('Digite o Angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print(f'O Angulo tem o Seno de {seno :.2F} ')
cosseno = math.cos(math.radians(angulo))
print(f'O Angulo tem o Cosseno de {cosseno :.2F} ')
tangente = math.tan(math.radians(angulo))
print(f'O Angulo tem a Tangente de {tangente :.2F} ')
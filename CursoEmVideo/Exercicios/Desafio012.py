print ('================= Desafio 12 =================')
preco = float(input('Digite o preço do produto:R$ '))
print(f'O produto que custava R$ {preco :.2f}, na promoção com 5% de desconto, vai custar R$: {preco - (preco * 5 / 100) :.2f}.')

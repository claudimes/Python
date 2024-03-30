contador = 0
preco_antigo = 0
preco_novo = 0
codigo = 0

while codigo >= 0:
    codigo = int(input('Digite o Codigo do produto:'))
    if codigo < 0:
        print(" ")
    else:
        preco = float(input('Digite o preço do produto: R$ '))
        contador = contador + 1
        aumento = (preco * 20) / 100
        preco_antigo = preco_antigo + preco
        preco_novo = preco_novo + preco + aumento
        print(f'Codigo {codigo}: Novo Preço: R$ {preco + aumento}')

media_preco_antigo = preco_antigo / contador
media_preco_novo = preco_novo / contador

print(f'Media preços antigos: R$ {media_preco_antigo} ')
print(f'Media preços novos: R$ {media_preco_novo}')




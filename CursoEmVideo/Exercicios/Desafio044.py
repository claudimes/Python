print('================= Desafio 44 =================')
print('================= LOJAS GOMES =================')
compra = float(input('Valor das Compras: R$ '))
print('''FORMAS DE PAGAMENTO:
( 1 ) à vista dinheiro/cheque
( 2 ) à vista cartão
( 3 ) 2x no cartão
( 4 ) 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = compra - (compra * 10/100)
else:
    if opcao == 2:
        total =compra - (compra * 5 / 100)
    else:
        if opcao == 3:
            total = compra
            parcela = total / 2
            print(f'Sua compra será parcelada em 2 vezes de R$ {parcela :.2f}.')
        else:
            if opcao == 4:
                total = compra + (compra * 20 / 100)
                totparc = int(input('Quanta parcelas? '))
                parcela = total / totparc
                print(f'Sua compra será parcelada em {totparc} x de R$ {parcela :.2f} COM JUROS.')
            else:
                total = compra
                print('OPÇÂO INVALIDA de pagamento. tente novamente!')
print(f'Sua Compra de R$ {compra :.2f} vai custar R$ {total :.2f}')

print('================= Desafio 37 =================')
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
( 1 ) converter para BINÁRIO
( 2 ) converter para OCTAL
( 3 ) converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINARIO é igual a {bin(num) [2:]}') #[2:] refrente a fatiamento de String, neste caso para não a aprecer as 2 letras antes da resposta
else:
    if opcao == 2:
        print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
    else:
        if opcao == 3:
            print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
        else:
            print('Opção invalida. Tente Novamente!')

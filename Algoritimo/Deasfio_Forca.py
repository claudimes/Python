# Colaborou: Claudio Gomes, Thiago Prata e Joao Victor Machado

from random import randint
from time import sleep

print('-=' * 12, '\033[1;34mFORCA\033[m', '-=' * 12)
sleep(1)
print('''\033[1m
 +--------+
 |            Desafie-se tentando descobrir qual é a palavra oculta
 |                antes que esgotem as suas Tentativas.
 |
 | 
 \033[m''')
sleep(1)
print('-=' * 10, '\033[1;36m Vamos Começar\033[m', '-=' * 10)

print('\033[1;31m 3... \033[m')
sleep(1)
print('\033[1;33m 2... \033[m')
sleep(1)
print('\033[1;32m 1... \033[m')
sleep(1)

print(f'-=' * 5, '\033[1;34mEscolha o Conjunto de Palavras a Serem Usadas\033[m', '-=' * 5)
escolha = int(input(f"\033[1;33m [1] Frutas [2] Nomes [3] Estados [4] Países:\033[m "))
conjunto = {}
jogo = ''
if escolha == 1:
    arquivo = open("Frutas.txt")
    linhas = arquivo.readlines()
    conjunto = ''
    while len(conjunto) < 3 or len(conjunto) > 10:
        sorteio = randint(0, len(linhas))
        conjunto = linhas[sorteio]
    conjunto = conjunto.upper().strip()
    arquivo.close()
    jogo: str = 'Fruta'
else:
    if escolha == 2:
        arquivo = open("Nomes.txt")
        linhas = arquivo.readlines()
        conjunto = ''
        while len(conjunto) < 3 or len(conjunto) > 10:
            sorteio = randint(0, len(linhas))
            conjunto = linhas[sorteio]
        conjunto = conjunto.upper().strip()
        arquivo.close()
        jogo: str = 'Nome'
    else:
        if escolha == 3:
            arquivo = open("Estados.txt")
            linhas = arquivo.readlines()
            conjunto = ''
            while len(conjunto) < 3 or len(conjunto) > 10:
                sorteio = randint(0, len(linhas))
                conjunto = linhas[sorteio]
            conjunto = conjunto.upper().strip()
            arquivo.close()
            jogo: str = 'Estado'
        else:
            if escolha == 4:
                arquivo = open("Paises.txt")
                linhas = arquivo.readlines()
                conjunto = ''
                while len(conjunto) < 3 or len(conjunto) > 10:
                    sorteio = randint(0, len(linhas))
                    conjunto = linhas[sorteio]
                conjunto = conjunto.upper().strip()
                arquivo.close()
                jogo: str = 'País'
# print(f'Palavra é {conjunto}')
print(f'\033[1m A Palavra é um(a) {jogo} e tem: {len(conjunto)} letras\033[m.')
print('-' * 55)

cont = 1
erro = 0
letra = acerto = duplicidade = ''

while True:
    escolha = ''
    while escolha != '1' and escolha != '2':
        escolha = str(input('Quer Digitar uma LETRA ou ARRISCAR a PALAVRA: [1] LETRA/[2] PALAVRA: ')).upper().strip()
    if escolha == "2":
        resposta = str(input('Qual é a PALAVRA? ')).upper().strip()
        if sorted(conjunto) == sorted(resposta):
            print('*' * 40)
            print('\033[1;32m Parabéns, você GANHOU!!!!')
            print(f'A PALAVRA era: {conjunto}\033[m')
            break
            print('*' * 40)
        else:
            print('Hum, Essa não é a Palavra.')
            print('\033[1;31m MORREU ENFORCADO!\033[m ')
            print(f'A PALAVRA era: {conjunto}\033[m')
            print('Você consegue fazer melhor!')
            print('''
                                +-------+
                                |       O
                                |      /|\.
                                |      / \,
                                |''')
            break
    else:
        if escolha == "1":
            while letra == '':
                letra = str(input(f'\033[1m {cont}ª PALPITE: Qual é a Letra? ')).upper().strip()
            print('-' * 40)
            if letra in acerto or letra in duplicidade:
                print(f'{letra} ja foi INFORMADA.')
                letra = ''
                print('-' * 40)
            else:
                cont += 1
                if letra in conjunto:
                    acerto += letra
                    palavra_formada = ''
                    for i in conjunto:
                        if i in acerto:
                            palavra_formada += i
                        else:
                            palavra_formada += '_'
                    print(f'\033[1;32m Palavra Formada --> {palavra_formada} \033[m')
                    if conjunto == palavra_formada:
                        print('*' * 40)
                        print('\033[1;32m Parabéns, você GANHOU!!!!')
                        print(f'A PALAVRA era: {conjunto}\033[m')
                        print('*' * 40)
                        break
                else:
                    print(f'A palavra não tem letra {letra}')
                    erro = erro + 1
                    duplicidade += letra
                    print(f'Esse foi seu \033[1;31m{erro}º erro.\033[m')
                    print('-' * 40)
                letra = ""
                if erro == 6:
                    print('=' * 40)
                    print('''
                    +-------+
                    |       O
                    |      /|\.
                    |      / \,
                    |''')
                    print(f'ERROU {erro} vezes.\033[1;31m MORREU ENFORCADO!\033[m ')
                    print('Você consegue fazer melhor!')
                    print(f'A PALAVRA era: {conjunto}\033[m')
                    print('=' * 40)
                    break
                if erro == 1:
                    print('''
                    +--------+
                    |        O
                    |        
                    |
                    |''')
                else:
                    if erro == 2:
                        print('''
                        +-------+
                        |       O
                        |       |
                        |
                        |''')
                    else:
                        if erro == 3:
                            print('''
                            +-------+
                            |       O
                            |      /|
                            |
                            |''')
                        else:
                            if erro == 4:
                                print('''
                                +-------+
                                |       O
                                |      /|\.
                                |
                                |''')
                            else:
                                if erro == 5:
                                    print('''
                                    +-------+
                                    |       O
                                    |      /|\.
                                    |      /
                                    |''')

                print('-' * 40)
    print(f'\033[1;40m LETRAS usadas: {acerto}{duplicidade} \033[m')
    print('-' * 40)

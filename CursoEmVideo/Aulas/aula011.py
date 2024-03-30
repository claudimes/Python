nome = str(input('Qual é seu Nome? '))
if nome == 'Claudio':
    print('Que nome lindo você tem!')
else:
    if nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
        print('Seu nome é bem popular no Brasil.')
    else:
        if nome in 'Claudia Jessica Juliana':
            print('Belo nome feminino')
        else:
            print('Seu nome é tão normal!')
print(f'Bom Dia, {nome}!')

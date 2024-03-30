#Formas de Fatiar Palavras
frase = 'Curso em Video Python'
print(frase[::2])

print('''Forma de Print para 
uma frase ou texto longo, não sendo necessario ficar inserido Print em cada linha .''')

print('Função Count ---> Conta a quantidade de letras Selecionada. OBS: A diferença entre MAIUSCULA e minuscula')
print(frase.count('o'))

print('Função Upper ---> Usada para deixar todas as letras MAIUSCULAS')
print(frase.upper().count('O'))

print('Função Len ---> Para saber o Tamanho da frase.')
print(len(frase))

print('Função strip ---> remove os espaço indesejados antes e depois da frase.')
print(len(frase.strip()))

print('Função replace ---> Substitui a palavra a ser exibida naquela exibição.')
print(frase.replace('Python', 'Android'))
print('Para alterar e salvar a substuição de palavra use o camando abaixo')
#frase = frase.replace('Python', 'Android')
#print(frase)
print('Para verificar se existe alguma palavra use:')
print('Curso' in frase)

print('Função Find ---> Localiza a posição inicial da palavra.')
print(frase.find('Video'))

print('Função Lower ---> Usada para deixar todas as letras minuscula.')
print(frase.lower().find('video'))

print('Função Split ---> Cria uma Lista com separador de espaço.')
print(frase.split())

print ('Estou dizendo: Pega o divido 2(que é video) me mostra a letra 3(e)')
dividido = (frase.split())
print(dividido[2][3])
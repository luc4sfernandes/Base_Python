# script6.py
arquivo = open("dados1.txt", "r")

# O método readlines() lê o arquivo inteiro e o transforma em uma LISTA.
# Cada linha do arquivo vira um item (string) dentro dessa lista.
conteudo = arquivo.readlines()

# Tipo da variável: aqui será <class 'list'>
print("Tipo do conteúdo:", type(conteudo))

# O repr() mostra a lista "crua". 
# Ex: ['Linha 1\n', 'Linha 2']
print("Conteúdo retornado pelo readlines:")
print(repr(conteudo))

# Fecha o arquivo para liberar o sistema
arquivo.close()

# Abre o arquivo para leitura
arquivo = open("dados1.txt", "r")

# Pega APENAS A PRIMEIRA LINHA do arquivo e salva na variável
# (Diferente do read(), ele para no primeiro \n que encontrar)
conteudo = arquivo.readline()

# Tipo da variável (será uma <class 'str'>)
print("Tipo do conteúdo:", type(conteudo))

# Exibe a representação real daquela linha específica
print("Conteúdo retornado pelo readline:")
print(repr(conteudo))

# ?? O QUE ACONTECE AQUI:
# O Python move um "cursor" após ler a primeira linha. 
# Ao chamar readline() de novo, ele lê a PARTIR de onde parou (a segunda linha).
proximo_conteudo = arquivo.readline()

print("Próximo Conteúdo retornado:")
print(repr(proximo_conteudo))

# Fecha o arquivo para liberar memória
arquivo.close()

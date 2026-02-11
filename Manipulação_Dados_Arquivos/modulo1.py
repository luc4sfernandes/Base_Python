import os

# Abrindo o arquivo no modo escrita
arquivo = open('exemplo1.txt', 'w')

# Exibindo os atributos do arquivo
print("Nome do arquivo:", arquivo.name) # --> Exibir nome do arquivo
print("Modo de abertura:", arquivo.mode) # --> Exibir modo de abertura do arquivo
print("Arquivo está fechado?", arquivo.closed) # --> Exibir se esta fechado o arquivo

# Escrevendo no arquivo
arquivo.write("Olá, mundo")

# Fechando o arquivo
arquivo.close()

# Verificando se o arquivo está fechado
print("Arquivo está fechado agora?", arquivo.closed)

# Exibindo caminhos relativo e absoluto
relpath = os.path.relpath('exemplo1.txt')
abspath = os.path.abspath('exemplo1.txt')

print("Caminho relativo:", relpath)
print("Caminho absoluto:", abspath)

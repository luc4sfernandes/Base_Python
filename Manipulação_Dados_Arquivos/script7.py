# script7.py
# Abre o arquivo no modo leitura ("r")
arquivo = open("dados1.txt", "r")

print("Iterando sobre o arquivo")

# Aqui está a "mágica": o objeto 'arquivo' é percorrido linha por linha
# Isso é muito mais eficiente em termos de memória do que o arquivo.read()
for linha in arquivo:
    # O repr(linha) mostra o conteúdo da linha atual incluindo o \n
    print(repr(linha))

# Fecha o arquivo para liberar recursos do sistema
arquivo.close()

# script4.py
# Abre o arquivo 'dados1.txt' apenas para leitura ("r")
arquivo = open("dados1.txt", "r")

# LÊ O ARQUIVO INTEIRO e armazena em uma única variável do tipo String
conteudo = arquivo.read()

# Mostra que a variável 'conteudo' é do tipo <class 'str'>
print("Tipo do conteúdo:", type(conteudo))

print("Conteúdo retornado pelo read:")
# Exibe a representação técnica da string (mostrando caracteres ocultos como \n)
print(repr(conteudo))

# Libera o arquivo para que outros programas possam usá-lo e economiza memória
arquivo.close()

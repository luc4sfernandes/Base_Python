import os

# 1. Abertura do arquivo no modo 'w' (write - escrita)
# Criamos o objeto 'arquivo' 
arquivo = open("dados1.txt", 'w', encoding='utf-8')

# 2. Obtendo o caminho absoluto (Caminho completo no SO)
print(f"Caminho Absoluto: {os.path.abspath(arquivo.name)}\n")

# 3. Escrita de dados
arquivo.write("Ola Mundo!!!")

# 4. Obtendo o caminho relativo
print(f"Caminho Relativo: {os.path.relpath(arquivo.name)}\n")

# 5. Representação do objeto e fechamento
print(arquivo)
arquivo.close() # Boas práticas: sempre fechar o stream de dados

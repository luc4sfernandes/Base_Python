# script8.py
arquivo = open("dados1.txt", "r")

# Guarda todo o conteúdo. O cursor vai para o FIM do arquivo.
conteudo = arquivo.read()
print("Todo o conteúdo do arquivo")
print(repr(conteudo), '\n')

# RELEITURA: O cursor já está no fim, então não lê nada (retorna '')
conteudo_releitura = arquivo.read()
print("Releitura de todo o conteúdo do arquivo")
print(repr(conteudo_releitura), '\n')

arquivo.close()

arquivo_reaberto = open("dados1.txt", "r")

conteudo_reaberto = arquivo_reaberto.read()
print("Todo o conteúdo do arquivo novamente")
print(repr(conteudo_reaberto), '\n')

# SEEK(0): Volta o cursor para o início do arquivo (posição zero)
arquivo_reaberto.seek(0)

# Agora o read() consegue ler tudo de novo porque o cursor "rebobinou"
conteudo_seek = arquivo_reaberto.read()
print("Todo o conteúdo do arquivo após o SEEK")
print(repr(conteudo_seek))

arquivo_reaberto.close()

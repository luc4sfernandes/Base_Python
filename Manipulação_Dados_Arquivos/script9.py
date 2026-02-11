# script9.py (Baseado no Script 10 das suas imagens)

# 1. ESTRUTURA NA RAM: Lista de Objetos String
# Os dados estão organizados em uma estrutura de lista, prontos para serem iterados.
linhas = [
    "Conteúdo da primeira linha.",
    "\nConteúdo da segunda linha."
]

# 2. OPERAÇÃO DE SISTEMA: Abertura em modo "w" (Write)
# O Python solicita ao SO a criação do arquivo. Se já existir, o conteúdo é TRUNCADO (apagado).
arquivo_escrita = open("dados_writelines.txt", "w")

# 3. TRANSFERÊNCIA: Gravação em Lote (Batch)
# O writelines percorre a lista e descarrega cada string no buffer do arquivo.
# Importante: ele não adiciona quebras de linha sozinho, você deve incluí-las (como o \n).
arquivo_escrita.writelines(linhas)

# 4. FINALIZAÇÃO: Flush e Close
# Garante que os dados saiam da memória temporária (buffer) e sejam salvos fisicamente no HD/SSD.
arquivo_escrita.close()

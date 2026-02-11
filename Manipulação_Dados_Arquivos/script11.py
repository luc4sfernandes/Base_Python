print("Iterando sobre o arquivo")

# 1. GERENCIADOR DE CONTEXTO (with):
# Abre o arquivo e garante que, ao sair deste bloco (por erro ou finalização),
# o Python execute o .close() automaticamente para você. 
with open("dados1.txt", "r") as arquivo:
    
    # 2. ITERAÇÃO POR LINHA (Eficiência de Memória):
    # O arquivo funciona como um 'gerador'. Ele lê a linha atual do disco,
    # coloca na RAM, o print a exibe, e ela é descartada para a próxima entrar.
    for linha in arquivo:
        # Nota: o print adiciona um \n, e a linha já tem um \n do arquivo.
        # Por isso você verá linhas em branco entre os textos no console.
        print(linha)

    # 3. ATRIBUTO .name:
    # Acessamos uma propriedade do objeto arquivo para mostrar o nome dele.
    print("Fim do arquivo", arquivo.name)

# A partir daqui, o arquivo já está fechado e seguro no disco.

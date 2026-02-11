import os

arquivo = open('texto.txt', 'w')

while True:
    try:
        decicao = int(input("1. Inserir uma Frase\n2. Inserir um Paragrafo\n3. Sair\n"))
        if decicao > 3:
            print("Opção invalida! Escolha uma opção disponivel...")
            os.system('clear')
            continue
    except ValueError:
        print("Opção invalida! Escolha uma opção disponivel...")
        os.system('clear')
        continue
      

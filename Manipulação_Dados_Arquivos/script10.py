# script10.py (Baseado no Script 11 das suas imagens)

# 1. MODO "a" (Append/Anexar): 
# Diferente do "w", ele não apaga o arquivo. 
# O Python abre o arquivo e move o CURSOR automaticamente para o final de tudo.
arquivo_escrita = open("dados_write.txt", "a")

# 2. ESCRITA DE DADOS:
# Como o cursor já está no fim, o write() apenas "empurra" novos bytes dali para frente.
# O \n garante que o texto comece em uma nova linha física no disco.
arquivo_escrita.write("\nConteúdo adicional.")

# 3. FECHAMENTO:
# Salva as alterações e libera o arquivo para outros processos.
arquivo_escrita.close()# script10.py (Baseado no Script 11 das suas imagens)

# 1. MODO "a" (Append/Anexar): 
# Diferente do "w", ele não apaga o arquivo. 
# O Python abre o arquivo e move o CURSOR automaticamente para o final de tudo.
arquivo_escrita = open("dados_write.txt", "a")

# 2. ESCRITA DE DADOS:
# Como o cursor já está no fim, o write() apenas "empurra" novos bytes dali para frente.
# O \n garante que o texto comece em uma nova linha física no disco.
arquivo_escrita.write("\nConteúdo adicional.")

# 3. FECHAMENTO:
# Salva as alterações e libera o arquivo para outros processos.
arquivo_escrita.close()

from hashlib import sha256

def critpgrafar_text():
    text = str(input("Qual texto você quer criptografar? "))
    hash_text = sha256(text.encode())
    hash_textvar = hash_text.hexdigest()
    print(hash_textvar)
    option_one = int(input("Você quer escrever essa criptografia em um arquivo?\n[1] - Sim\n[2] - Não\n"))
    if option_one == 1:
        with open("text.txt" , 'w') as file:
            file.write(hash_textvar)
            enter = input("Pressione enter, para continuar......")

def criptografar_file():
    file_name = str(input("Qual é o nome do arquivo? Coloque txt no final, porfavor: "))
    with open(f"{file_name}", "r") as file:
        conteudo = file.read()
        conteudo_cript = sha256(conteudo.encode())
        conteudo_text = conteudo_cript.hexdigest()
        print(conteudo_text)
        with open(f"{file_name}", "w") as file: 
            file.write(conteudo_text)
            input("Deu tudo certo. Pressione enter para continuar.....")        
option_one = int(input("Você quer criptografar uma arquivo ou um texto?\n[1] - Arquivo\n[2] - Texto\n"))
if option_one == 2:
    critpgrafar_text()
else:
    criptografar_file()

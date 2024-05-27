def criaArquivo(texto):
    try:
        with open("novo1.txt", "r+") as arquivo:
            conteudo = arquivo.readlines()
            conteudo.append(texto + "\n")
            arquivo.close()
        arquivo = open("novo1.txt", "w")
        arquivo.writelines(conteudo)
        arquivo.close()
    except Exception as e:
        print("Falha ao abrir arquivo: {}".format(e))


def lerArquivo():
    conteudo = open("novo1.txt", "r")
    print(conteudo.read())
    conteudo.close

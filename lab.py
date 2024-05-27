import exercicio4, os
sair = False

while sair == False:
    opcao = input("Escolha uma opação: \n"
                  "1: Cadastrar item\n"
                  "2: Listar itens\n"
                  "3: Sair\n")
    if opcao == "1":
        item = input("Digite o item a ser adicionado: ")
        exercicio4.criarArquivo(item)
    elif opcao == "2":
        exercicio4.lerArquivo()
    elif opcao == "3":
        sair = True
    else:
        print("Opção invalida")


    #os.system('cls')
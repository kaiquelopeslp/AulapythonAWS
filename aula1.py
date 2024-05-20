def boasVindas(nome, idade):
    print("Olá {}, nem parece que você tem {} anos". format(nome, idade))

def ePar(numero):
    print(numero%2)
    if (numero%2)  == 0:
        print("{} é par".format(numero))
    else:
        print("{} é impar".format(numero))



if __name__== "__main__":
    #nome = input("Qual seu nome? ")
    #idade = int(input("Qual sua idade? "))
    #boasVindas(nome, idade)
    numero = (int(input("Digite o número: ")))
    ePar(numero)
git config --global user.name "kaiquelopeslp" git config --global user.email kaiquelopeslp@gmail.com
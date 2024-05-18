'''Sabendo que a area de um triangulo é igual a base * altura / 2
Crie uma função para que receba a base e a altura e retorne a area'''


def CalcularBaseAltura(base, altura):
    area = (base*altura) / 2
    return area




if __name__ == '__main__':
    base = float(input("Digite a base do triangulo: "))
    altura = float(input("Digite a altura do triangulo: "))
    areatriangulo = CalcularBaseAltura(base, altura)
    print("A área do triângulo é:", areatriangulo)
'''Sabendo que a area de uma circunferência é calculada com 2pi * r ao quadrado, crie uma função para retornar a area da circuferência'''


def calcularareacircunferencia(raio):
    pi=3.14
    return pi*raio**2


if __name__ == "__main__":
    print(calcularareacircunferencia(float(input("Digite o raio da circuferência: "))))
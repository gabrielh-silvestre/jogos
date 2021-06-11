from calculos import Calculos
from comodo import Comodo

calc = Calculos()


def montando_comodo(vez):
    print(f"Vamos para o {vez}º comodo.\n")

    comprimento = float(input("Qual o comprimento do comodo em metros? "))
    largura = float(input("E a largura? "))
    comod = Comodo(comprimento, largura)

    print(f"\nA área das paredes são de {calc.calcular_parede(comprimento, comod.parede_altura):.2f}m².")
    print(f"A área do teto é de {calc.calcular_teto(comprimento, largura):.2f}m².")

    tinta = calc.tinta_gasta()
    print(f"Seu gasto de tinta será de {tinta:.2f}l.\n")


def pintar(n):
    i = 1
    while i <= n:
        montando_comodo(i)
        i += 1
    else:
        print("Belo trabalho, por hoje terminamos por aqui!")


if __name__ == "__main__":
    n_comodos = int(input("Quantos comodos iremos pintar? "))
    pintar(n_comodos)

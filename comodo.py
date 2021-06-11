from calculos import Calculos


class Comodo(Calculos):
    def __init__(self, comprimento, teto_largura):
        self.__parede_altura = 2.9
        self.__comprimento = comprimento
        self.__teto_largura = teto_largura

    @property
    def parede_altura(self):
        return self.__parede_altura

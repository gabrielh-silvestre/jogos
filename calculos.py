class Calculos:
    __area_parede = float
    __area_teto = float

    def calcular_parede(self, eixo_x, eixo_y):
        self.__area_parede = eixo_x * eixo_y
        return self.__area_parede

    def calcular_teto(self, eixo_x, eixo_y):
        self.__area_teto = eixo_x * eixo_y
        return self.__area_teto

    def tinta_gasta(self):
        return (self.__area_parede + self.__area_teto) / 10

    @property
    def area_parede(self):
        return self.__area_parede

    @property
    def area_teto(self):
        return self.__area_teto


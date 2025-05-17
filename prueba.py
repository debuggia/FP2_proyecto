class Componentes:
    def __init__(self, codigo, nombre, precioCom):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precioCom = precioCom

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, nvoDato):
        self.__codigo = nvoDato

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nvoDato):
        self.__nombre = nvoDato

    @property
    def precioCom(self):
        return self.__precioCom

    @precioCom.setter
    def precioCom(self, nvoDato):
        self.__precioCom = nvoDato

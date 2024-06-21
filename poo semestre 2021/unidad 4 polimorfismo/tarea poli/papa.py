import abc
from abc import ABCMeta
class medirterreno:
    __metaclass__=ABCMeta

    def inicio(self):
        print"bienvenido"
        print"medicion de terreno"

    @abc.abstractmethod
    def medirperimetro(self):
        pass

    @abc.abstractmethod
    def medirarea(self):
        pass

    def cobro(self):
        print"$10 por m2 (area)"
        print"$5 por m (perimetro)"
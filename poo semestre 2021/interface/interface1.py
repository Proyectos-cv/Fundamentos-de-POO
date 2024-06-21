import abc
from abc import ABCMeta
#una interfaz solo lleva funciones abstractas, es decir, sin cuerpo
class PadreInterface():
    __metaclass__ = ABCMeta
    # Con esto hago que una clase sea abstracta
    @abc.abstractmethod
    def pidiendo(self):
        pass
    @abc.abstractmethod
    def calculando(self):
        pass
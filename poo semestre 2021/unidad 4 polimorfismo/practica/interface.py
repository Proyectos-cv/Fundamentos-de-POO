import abc
from abc import ABCMeta
class inter:
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def llenar(self):
        pass

    @abc.abstractmethod
    def mostrar(self):
        pass
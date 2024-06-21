import abc
from abc import ABCMeta
class Animal():
    #con esto se hace una clase abstracta
    __metaclass__=ABCMeta
    #con esto se hace una funcion abstracta 
    @abc.abstractmethod
    def habitad(self):
        pass
    def msj(self):
        print"hola"
animal=Animal()
Animal.msj()
animal.habitad()
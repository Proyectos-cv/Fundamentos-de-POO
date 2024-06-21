import abc
from abc  import ABCMeta
class Animalito:
    __metaclass__=ABCMeta
    #@abc.abstractmethod
    def habitad(self):
        pass
    def desplazamiento(self):
        pass
    def datos(self):
        self.nom = raw_input("Animal: ")
        self.espe = raw_input("Especie: ")
    def mostrar(self):
        print "NOMBRE: ", self.nom
        print "ESPECIE: ", self.espe

from arreglo import arreglo
from numpy import *
class eje(arreglo):
    def sumatradicional(self):
        u=int(input("amplitud del arreglo: "))
        s=self.usuario(u)
        print""
        print"arreglo final"
        print s
k=eje()
k.sumatradicional()

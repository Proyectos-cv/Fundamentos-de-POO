from numpy import *
from examen import fun
class arre:
    def __init__(self):
        self.fu=fun(self)
    def inicia(self):
        num=int(input("dimension de el arreglo: "))
        arreglo=zeros(num)
        self.fu.__init__(arreglo)

        print arreglo
sa=arre()
sa.inicia()
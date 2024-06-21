from interface import inter
from numpy import *
import random as r
class di15(inter):

    def llenar(self):
        print""
        print"numeros divisibles entre 15"
        i = int(input("dimension del arreglo: "))
        self.l = zeros(i)
        u = 0
        while u < i:
            a = r.randrange(1, 100)
            if a % 15 == 0:
                self.l[u] = a
                u = u + 1
    def mostrar(self):
        print self.l

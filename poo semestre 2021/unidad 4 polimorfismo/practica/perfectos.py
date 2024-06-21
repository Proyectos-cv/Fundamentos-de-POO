from interface import inter
from numpy import *
import random as r
class deficientes(inter):
    def llenar(self):
        print""
        print"numeros deficientes"
        i = int(input("dimension del arreglo: "))
        self.l = zeros(i)
        u = 0
        while u < i:
            a = r.randrange(2, 100)
            l=0
            for j in range(1, a):
                if a % j == 0:
                    l=l+j
            if l < a:
                self.l[u] = a
                u = u + 1
    def mostrar(self):
        print self.l

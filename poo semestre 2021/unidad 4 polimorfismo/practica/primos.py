from interface import inter
from numpy import *
import random as r
class prim(inter):

    def llenar(self):
        print"numeros primos"
        i=int(input("dimension del arreglo: "))
        self.l=zeros(i)
        u=0
        while u<i:
            n = 0
            a=r.randrange(1,100)
            for j in range (2,a):
                if a%j==0:
                    n=n+1
            if n==0:
                self.l[u]=a
                u=u+1
    def mostrar(self):
        print self.l

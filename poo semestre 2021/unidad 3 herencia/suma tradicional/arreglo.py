from numpy import *
import random as r
class arreglo:
    def usuario(self, u):
        #u = int(input("arreglo: "))
        print "creando arreglo 1"
        p = 1
        while p < 2:
            self.a = zeros(u)
            for i in range(u):
                self.a[i]=int(input("ingresa un dato (1-9): "))
                #self.a[i] = r.randrange(100)
            print self.a
            p = p + 1
        o = 1
        print"creando arreglo 2"
        while o < 2:
            self.k = zeros(u)
            for i in range(u):
                self.k[i]=int(input("ingresa un dato (1-9): "))
                #self.k[i] = r.randrange(100)
            print self.k
            o = o + 1

        print""
        print"arreglo de menor a mayor"
        for g in range(u - 1):
            for y in range(u - 1):
                if self.a[y] > self.a[y + 1]:
                    aux = self.a[y]
                    self.a[y] = self.a[y + 1]
                    self.a[y + 1] = aux
        print self.a

        print"arreglo de mayor a menor"
        for t in range(u - 1):
            for n in range(u - 1):
                if self.k[n] < self.k[n + 1]:
                    aux = self.k[n]
                    self.k[n] = self.k[n + 1]
                    self.k[n + 1] = aux
        print self.k

        self.s = zeros(u)
        x = 0
        for b in range(u - 1, -1, -1):
            e = self.a[b] + self.k[b]
            if e >= 10 and b > 0:
                w = e % 10
                j = e // 10
                self.s[b] = w
                self.a[b - 1] = self.a[b - 1] + j
            else:
                self.s[b] = e
        return self.s
        #print self.s
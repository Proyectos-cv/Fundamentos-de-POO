from numpy import *
import random as r
class crear:
    def iniciaarre(self, n):
        self.a=zeros(n)
        for i in range (n):
            self.a[i]=r.randrange(100)
        return self.a
    def aleatorio(self, n):
        for i in range (n):
            self.a[i]=r.randrange(100)
        return self.a


    def usuario(self):
        u=int(input("arreglo: "))
        print "arreglo 1"
        p=1
        while p<2:
            self.a = zeros(u)
            for i in range(u):
                self.a[i] = r.randrange(100)
            print self.a
            p=p+1
        o=1
        print"arreglo 2"
        while o<2:
            self.k = zeros(u)
            for i in range(u):
                self.k[i] = r.randrange(100)
            print self.k
            o = o + 1

        print"arreglo de menor a mayor"
        for g in range(u-1):
            for y in range(u-1):
                if self.a[y]>self.a[y+1]:
                    aux=self.a[y]
                    self.a[y]=self.a[y+1]
                    self.a[y+1]=aux
        print self.a

        print"arreglo de mayor a menor"
        for t in range(u-1):
            for n in range(u-1):
                if self.k[n] < self.k[n + 1]:
                    aux = self.k[n]
                    self.k[n] = self.k[n + 1]
                    self.k[n+1] = aux
        print self.k


        self.s=zeros(u)
        x=0
        for b in range(u-1,-1, -1):
            e=self.a[b]+self.k[b]
            if e>=10 and b>0:
                w=e%10
                j=e//10
                self.s[b]=w
                self.a[b-1]=self.a[b-1]+j
            else:
                self.s[b] = e
        print self.s




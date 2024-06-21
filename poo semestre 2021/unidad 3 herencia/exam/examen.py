from numpy import *
import random as r
class exa:
    def usuario(self):
        print"BIENVENIDO"
        q = int(input("dimencion arreglo: "))
        arre = zeros(q)
        l=0
        p=0
        g=0
        t=0
        for i in range(q):
            arre[i]=int(input("numero en el arreglo: "))
        print arre
        for j in range(q):
            if arre[j]%2==0:
                p=arre[j]+p
                l=l+1
            else:
                g=arre[j]+g
                t=t+1
        h=p/l
        k=g/t
        f = raw_input("dame primer jugador (pares): ")
        a = raw_input("dame segundo juagdor (impares): ")
        if h>k:
            print"ganador:",f,"con promedio de:",h
        elif h<k:
            print"ganador:",a,"con promedio de:",k
        else:
            print"empate"












    def azar(self):
        q=int(input("dimencion arreglo: "))
        arre=zeros(q)
        for i in range(q):
            arre[i]=r.randrange(100)
        print arre
    def siete(self):
        q = int(input("dimencion arreglo: "))
        arre = zeros(q)
        d=0
        while d < q:
            z=r.randrange(100)
            if z%7==0 and z!=0:
                arre[d]=z
                d=d+1
            else:
                pass
        print arre
    #def lista(self):
        #l=[]
        #l.append(int(input("dame un numero: ")))
        #l.append(int(input("dame un numero: ")))
        #print l
        #print l[0]
#s=exa()
#c=s.azar()
#n=s.usuario()
#m=s.siete()
#g=s.lista()
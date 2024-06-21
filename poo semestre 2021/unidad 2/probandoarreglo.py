from numpy import *
from operacionesarreglos import operacionarre
class probararre:
    def __init__(self):
        self.o = operacionarre()
        #self.arreg=zeros(9)
        #print self.arreg
        #self.l=operacionarre()
    def iniciaarre(self):
        #return self.arreg
        self.arre = zeros(9)
        print self.arre
        #print a
        #return a
        #self.o.buscar(a)
    def menu(self):
        #a = zeros(9)
        bandera = True
        while bandera==True:
            print "buscar 1"
            print "cambiar 2"
            print "eliminar 3"
            print "insertar 4"
            n=int(input("que quieres hacer?"))
            if n==1:
                print self.arre
                bandera=True
                uno = int(input("que numero quieres buscar?: "))
                self.o.buscar(self.arre, uno)
                #return uno
                #self.l.buscar(uno, a)
            elif n==2:
                bandera=True
                dos=int(input("que numero quieres cambiar?: "))
                tres = int(input("por cual numero lo quieres cambiar?: "))
                #self.o.cambiar(dos, tres, a)
                #return dos
                #return tres
            elif n==3:
                bandera=True
                cuatro=int(input("que numero quieres eliminar?: "))
                #self.o.eliminar(cuatro, a)
                #return cuatro
            elif n==4:
                bandera=True
                cinco=int(input("que numero quieres insertar?: "))
                seis = int(input("en que posicsion lo quieres?: "))
                #self.o.insertar(cinco, seis, a)
                #return cinco
                #return seis
            else:
                bandera=False
p= probararre()
eje=p.iniciaarre()
ejes=p.menu()
#op=operacionarre()
#op.buscar()
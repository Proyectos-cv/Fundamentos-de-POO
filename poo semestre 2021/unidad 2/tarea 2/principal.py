from numpy import *
from operacionmatriz import matriz
class principalmatrices:
    def __init__(self):
        self.m=matriz()
    def iniciamat(self):
        self.mat= zeros((3, 3))
    def menu(self):
        bandera = True
        while bandera == True:
            print "llenar aleatoriamente.........1"
            print "llenar con divisibles de 7....2"
            print "llena con numeros primos......3"
            print "llena el usuario..............4"
            n = int(input("que quieres hacer?"))
            if n == 1:
                self.m.llenaalea(self.mat)
                bandera = True
            elif n == 2:
                self.m.llenadiv7(self.mat)
                bandera = True
            elif n == 3:
                self.m.llenaprimos(self.mat)
                bandera = True
            elif n == 4:
                self.m.llenaUsua(self.mat)
                bandera = True
            else:
                bandera = False
pri=principalmatrices()
un=pri.iniciamat()
ele = pri.menu()
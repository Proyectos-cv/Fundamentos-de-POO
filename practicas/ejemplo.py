# -*- coding: utf-8 -*-
# #!/usr/bin/env python
from OperaArre import Operaciones
from numpy import *
class Principal:
    def __init__(self, msj):
        print msj
        self.oa=Operaciones()
    def inicia(self):
        self.arre=zeros(10)
    def menu(self):
        print "Insertar ......[1]"
        print "Buscar.........[2]"
        print "Salir .........[5]"
        opc=int(input("Qué deseas hacer: "))
        if opc==1:
            print "INSERTAR"
            dato=int(input("Qué dato deseas insertar: "))
            pos=int(input("Dame la posición: "))
            #print "Probando: ", self.arre
            self.oa.insertar(self.arre, dato, pos)
p=Principal("Bienvenido a operaciones con Arreglos")
p.inicia()
p.menu()

# -*- coding: utf-8 -*-
# #!/usr/bin/env python
from muestraArre import Mostrar
class Operaciones:
    def __init__(self):
        self.mostra=Mostrar()
    def insertar(self, arre, dato, pos):
        self.arre=arre
        #print "Probando: ", self.arre
        self.arre[pos]=dato
        self.mostra.muestra(self.arre)


# -*- coding: utf-8 -*-
# #!/usr/bin/env python
class Mostrar:
    def __init__(self):
        pass
    def muestra(self, arre):
        for i in range (10):
            print arre[i], "  ",

print('\033[35m'), #Esta linea te da el texto en color el 35 es el color
print "\nInsertar.....[1]"
print "Buscar.......[2]"
print "Cambiar......[3]"
print "Eliminar.....[4]"
print "Salir........[5]"
opcion= int(input( "Qué deseas hacer: "))
print('\033[39m') #Esta linea te regresa al color por default el 39 es el color negro
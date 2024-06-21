from mostrararreglo import muestraarre
class operacionarre:
    def __init__(self):
        self.m=muestraarre()
    def buscar(self, arre, uno):
        for i in range (9):
            self.a=arre
            print self.a
            if self.a[i] == uno:
                aux=i
                print "encontrado en la posicion: ",aux
                self.m.mostrararre(self.a)
                #return a
            else:
                print "no encontrado"
    def cambiar(self, a, dos, tres):
        for i in range (9):
            if a[i]== dos:
                a[i]=tres
                self.m.mostrararre(a)
    def eliminar(self, a, cuatro):
        for i in range (9, cuatro):
            if a[i]== cuatro:
                a[i]= 0
                self.m.mostrararre(a)
    def insertar(self, a, seis, cinco):
        for i in range (9):
            if i== seis:
                a[i]=cinco
                self.m.mostrararre(a)
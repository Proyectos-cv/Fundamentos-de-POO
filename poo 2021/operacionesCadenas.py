from cadenas import Cad

class OperaCadenas:
    def __init__(self):
        print "Esta en "
        self.c=Cad()

    def longitud(self, cad):
        l=len(cad)
        #print "longitud ", l
        self.c.mostrar(l)
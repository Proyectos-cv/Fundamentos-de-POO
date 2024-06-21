from interface1 import PadreInterface

class Hija1Inter(PadreInterface):
    def __init__(self):
        print "Hija 1"
    def pidiendo(self):
        print "Le estoy poniendo cuerpo a esta funcion"
    def calculando(self):#si falta una no corre el programa
        pass
h=Hija1Inter()
from papa import Padre
class H2(Padre):
    def __init__(self, msj):
        print "Hola hija 2", msj
        Padre("el constructor del padre en Hija2")#de la hi ja al padre solo con el nombre del padre 
from papa import Padre
class Hija1(Padre):

    def __init__(self, msj):
        print "Hola hija ", msj
        Padre("el constructor del padre")
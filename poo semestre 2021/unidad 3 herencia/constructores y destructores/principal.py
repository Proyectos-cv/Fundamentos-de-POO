from hij1 import Hija1
from hij2 import H2

class Principal:
    def __init__(self, msj):
        print "Hola principal ", msj
        h=Hija1("aqui se ejecuta el constructor de la hija")
        #h.mensajes()
        hi2=H2("en hija 2")#de principal a hija instanciacion
        #hi2.mensajes()

p=Principal(" este es mi constructor")
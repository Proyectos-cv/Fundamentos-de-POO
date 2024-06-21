from operacionesCadenas import OperaCadenas

class Principal:
    def __init__(self):
        print "Bienvenido a mi programa"
    def inicia(self):
        cadena=raw_input("Dame una cadena")
        return cadena

p=Principal()
cad= p.inicia()
opCad=OperaCadenas()
opCad.longitud(cad)
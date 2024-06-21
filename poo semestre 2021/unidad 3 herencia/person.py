class personas:
    nom=""
    dom=""
    edad=0
    def pedirdatos(self):
        global nom, dom, edad
        nom=raw_input("dame tu nombre: ")
        dom = raw_input("dame tu domicilio: ")
        edad = raw_input("dame tu edad: ")
    def mostrardatos(self,tipo):
        print"nombre del ",tipo,": ", nom
        print"domicilio: ",dom
        print"edad: ",edad
from exeptusuario import miexepcion
class probando:
    def prueba(self):
        try:
            edad=int(input("dame tu edad:"))
            if edad<18:
                raise miexepcion
            else:
                print"eres mayor de edad"
        except miexepcion as e:
            print miexepcion, e

p=probando()
p.prueba()
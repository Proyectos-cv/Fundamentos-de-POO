from tarea2 import heren
class proceso(heren):
    def operacion(self):
        p = int(input("dame un numero base: "))
        t = int(input("dame un numero de exponente: "))
        s=p**t
        print "el numero",p,"elevado a",t,"es:",s

op=proceso()
op.operacion()
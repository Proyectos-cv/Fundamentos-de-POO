from datos import dato
from promedios import mater
class control(dato, mater):
    def __init__(self):
        print"BIENVENIDO A CONTROL ESCOLAR"
        print"DATOS DE CAPTURA DE ESTUDIANTES"
        print"isc........[1]"
        print"iem........[2]"
        self.q=int(input("carrera: "))
        if self.q==1:
            print"******* INGENIERIA EN SISTEMAS COMPUTACIONALES *********"
        elif self.q==2:
            print"******* INGENIERIA ELECTROMECANICA ************"
    def dat(self):
        r=int(input("numero de control: "))
        t = raw_input("nombre: ")
        u = int(input("edad: "))
        i = raw_input("direccion: ")
        o = raw_input("carrera: ")
        print"numero de control: ",r
        print"nombre: ",t
        print"edad: ",u
        print"direccion: ",i
        print"carrera: ",o
    def materias(self):
        self.pres()
        if self.q==1:
            self.isc()
        elif self.q==2:
            self.iem()
    def isc(self):
        print"calculo integral.....[1]"
        print"programacion.........[2]"
        print"base de datos........[3]"
        self.c=int(input("materia a evaluar: "))
        self.promisc()
    def iem(self):
        print"electronica..........................[1]"
        print"calculo..............................[2]"
        print"sistema electrico de potencia........[3]"
        self.k = int(input("materia a evaluar: "))
        self.promiem()
    def promisc(self):
        a=int(input("calificacion de la evaluacion: "))
        l = int(input("calificacion del proyecto: "))
        p = int(input("calificacion de la participacion: "))
        d= ((a*.4)+(l*.4)+(p*.2))
        if self.c==1:
            print"promedio de la materia calculo integral: ",d
        if self.c == 2:
            print"promedio de la materia programacion: ", d
        if self.c == 3:
            print"promedio de la materia base de datos: ", d
    def promiem(self):
        a = int(input("calificacion de la evaluacion: "))
        l = int(input("calificacion del proyectos: "))
        d = ((a * .3) + (l * .7))
        if self.k == 1:
            print"promedio de la materia electronica: ", d
        if self.k == 2:
            print"promedio de la materia calculo: ", d
        if self.k == 3:
            print"promedio de la materia sistema electrico de potencia: ", d
g=control()
g.dat()
g.materias()
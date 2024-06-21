from student import estudiantes
from employee import empleado

class prueba:
    def __init__(self):
        print"bienvenido a la herencia"
    def call(self):
        print"estudiante........[1]"
        print"empleado..........[2]"
        op=int(input("cual es tu opcion: "))
        if op==1:
            est=estudiantes()
            est.pedirdatos()
            est.mostrardatos("estudiante")
            c1=int(input("calificacion 1: "))
            c2=int(input("calificacion 2: "))
            c3=int(input("calificacion 3: "))
            est.promedio(c1, c2, c3)
        else:
            emp=empleado()
            emp.pedirdatos()
            emp.mostrardatos("empleado")
            emp.calcula()
            #hrs=int(input("horas trabajadas: "))
            #precio=int(input("precio por hora: "))
            #recompensa=int(input("compensacion en porcentaje: "))
            #emp.salario(hrs, precio, recompensa)
t=prueba()
t.call()
from person import personas
from salario import salari
class empleado(personas, salari):
    def __init__(self):
        print "clase empleados"
    def salario(self, hrs, precio,compensa):
        sueldo=hrs*precio
        compensacion= (compensa*10/100)+sueldo
        print "el sueldo es: ",sueldo
        print "el sueldo total es: ",compensacion


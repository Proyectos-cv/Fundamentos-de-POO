from promedio import CalculaProm

class Porcentajes(CalculaProm):
    def __init__(self):
        print "Promedios por Porcentajes"
    #aplicando la redefinicion
    def promedio(self):
        CalculaProm().promedio()
        cal1=int(input("Dame calif del examen: "))
        cal2 = int(input("Dame calif del proyecto: "))
        cal3 = int(input("Dame calif de tareas: "))
        prom= cal1 * .4 + cal2 * .3 + cal3 * .3
        print "Promedio: ", prom

por=Porcentajes()
por.promedio()
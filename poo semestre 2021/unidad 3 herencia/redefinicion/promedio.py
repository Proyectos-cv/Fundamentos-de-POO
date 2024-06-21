#clase padre
class CalculaProm:
    def promedio(self):
        cal1=int(input("Dame calificacion: "))
        cal2 = int(input("Dame calificacion: "))
        cal3 = int(input("Dame calificacion: "))
        promedio= (cal1 + cal2 + cal3) / 3
        print "Tu promedio es: ", promedio
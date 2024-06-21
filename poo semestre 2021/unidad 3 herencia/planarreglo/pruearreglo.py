from hacerarreglo import crear
class ProbandoHerencia(crear):
    def __init__(self):
        print "Probando a la clase Padre Arreglo"
    def mayor(self):
        n=int(input("De que size quieres al arreglo: "))
        a=self.iniciaarre(n)
        print self.a
        mayor=0
        for i in range(n):
            if a[i]>mayor:
                mayor=a[i]
        print "Mayor= ", mayor



    def sumatradicional(self):
        self.usuario()
        #print self.a
p=ProbandoHerencia()
#p.mayor()
p.sumatradicional()
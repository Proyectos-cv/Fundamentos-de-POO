from file1 import operaciones1
from file2 import operaciones2
class probando:
    def __init__(self):
        print"ejemplo de polimorfismo"
    def llamando(self):
        p1=operaciones1()
        print"suma=",p1.suma()
        p2=operaciones2()
        print"suma=",p2.suma(15, 10)
p=probando()
p.llamando()
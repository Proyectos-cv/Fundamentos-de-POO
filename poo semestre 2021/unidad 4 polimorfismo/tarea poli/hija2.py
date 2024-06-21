from papa import medirterreno
class terrenotriangular(medirterreno):
    def triangulo(self):
        print""
        self.inicio()
        self.cobro()
        print "triangulo equilatero"
        self.a=int(input("dame medida de base: "))
        self.s = int(input("dame medida de la altura: "))
    def medirperimetro(self):
        print""
        print "perimetro triangulo equilatero"
        w=(self.a)*3
        f = (w * 5)
        print"total pago de perimetro: ""$",f
        print"perimetro calculado",w,"m"

    def medirarea(self):
        print""
        print "area triangulo equilatero"
        w=(self.s * self.a)/2
        f = (w * 10)
        print"total pago de area: ""$",f
        print"area calculada", w,"m2"

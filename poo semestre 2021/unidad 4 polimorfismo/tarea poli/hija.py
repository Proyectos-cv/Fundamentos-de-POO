from papa import medirterreno
class terrenocuadrado(medirterreno):
    def cuadrado(self):
        self.inicio()
        self.cobro()
        self.a=int(input("medida del lado: "))
    def medirperimetro(self):
        print""
        print"perimetro cuadrado"
        w=self.a*4
        f = (w * 5)
        print"total pago de perimetro: ""$", f
        print"perimetro calculado: ", w,"m"

    def medirarea(self):
        print""
        print"area cuadrado"
        w=self.a*self.a
        f = (w * 10)
        print"total pago de m2: ""$", f
        print"area calculada", w,"m2"

import numpy
class criba:
    def cribar(self):
        cuantos = int(input("cuantos: "))
        arre1=numpy.zeros(cuantos)
        arre2 = numpy.zeros(cuantos)
        num=3
        for i in range(0,cuantos):
            arre1[i]= num
            arre2[i] = num
            num=num+2
        band=True
        x=0
        while band==True:
            salto=0
            print "x",x
            if arre2[x]!=0:
                aux = 0
                salto = int((cuantos - (x + 1)) / (arre2[x]))
                for i in range(0,salto):
                    aux=int(aux+arre2[x])
                    print"aux", aux
                    print"salto", salto
                    arre2[aux+x] = 0

            elif salto<=0:
                band=False
            x = x + 1



        print arre1
        print arre2
    def red(self):
        num1=7/9
        num2=3.2
        print(int(num1))
        print(int(num2))
c=criba()
c.cribar()
#c.red()
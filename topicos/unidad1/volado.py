import random
class volado:
    def arroja(self):
        #monedero=30
        #apuesta=10
        #gana=0
        #pierde=0
        #x=0
        #gane=0
        #perdi=0
        c=0
        gane = 0
        perdi = 0
        e=int(input("numero de iteraciones: "))
        while c<e:
            monedero = 30
            apuesta = 10
            gana = 0
            pierde = 0
            x = 0
            while monedero<50 and monedero>0:
                aleatorio=random.randrange(1,3)
                if aleatorio==1:
                    monedero=monedero+apuesta
                    apuesta=10
                    gana=gana+1
                    x=x+1
                elif aleatorio==2:
                    monedero=monedero-apuesta
                    apuesta=apuesta*2
                    pierde=pierde+1
                    x=x+1

            if monedero>=50:
                gane=gane+1
                c=c+1
            elif monedero<=0:
                perdi=perdi+1
                c=c+1
        print "veces ganadas: ", gane
        print "veces perdidas: ",perdi
        print "iteraciones realizadas: ",c
        c=float(c)
        gane=float(gane)
        probabilidad = float(gane / c)
        print"probabilidad: ", probabilidad

        #print "dinero total al final: ",monedero
        #print gana
        #print pierde


v=volado()
v.arroja()
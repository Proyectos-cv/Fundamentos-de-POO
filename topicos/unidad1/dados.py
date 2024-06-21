import random
class dado:
    def comienzo(self):
        monedero=20
        probabilidad=float(0)
        x=float(0)
        n=int(input("valor de n: "))
        while x < n and monedero<50 and monedero>0:
            #print ""
            #print x
            #print""
            detector=0
            suma = random.randrange(2,13)
            #print "1",suma
            if (suma == 7 or suma == 11) and detector==0:
                monedero = monedero + 1
                x = x + 1
                probabilidad=probabilidad+1
            elif (suma == 2 or suma ==3 or suma==12) and detector == 0:
                monedero=monedero-1
                x = x + 1
            elif suma==4 or suma==5 or suma==6 or suma==8 or suma==9 or suma==10:
                referencia = suma
                band=True
                while band==True:
                    suma = random.randrange(2, 13)
                    #if suma==7 or suma==2 or suma==3 or suma==11 or suma==12:
                    if suma==7:
                        monedero=monedero-1
                        band=False
                        x = x + 1

                    elif suma==referencia:
                        monedero=monedero+1
                        probabilidad = probabilidad + 1
                        band=False
                        x = x + 1
           # x=x+1
        print""
        print "veces ganadas: ",probabilidad
        prob=float(probabilidad/x)
        print "total de iteraciones: ",x
        print "probabilidad de ganar: ",prob*100,"%"
        print""
            #print "2",suma
            #print monedero






d=dado()
d.comienzo()
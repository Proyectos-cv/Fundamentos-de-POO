import random
class ruleta:
    def jugador1(self):
        monedero = 200
        x = 0
        n = int(input("valor de n: "))
        while x < n and monedero > 0:
            color = random.randrange(1,23)
            print "numero aleatorio del color: ",color
            if color > 0 and color<=10:
                print"gana la ronda"
                monedero=monedero+1
            elif color > 10 and color <=20:
                monedero=monedero-1
                print"pierde la ronda"
            elif color > 20 and color<=22:
                color = random.randrange(1,21)
                if color > 0 and color<=10:
                    print "empate"
                elif color > 10 and color<=20:
                    print"perdio en casilla verde"
                    monedero=monedero-1
            x=x+1
            #print color
            print "total: ",monedero

    def jugador2(self):
        monedero = 200
        aumento=1
        x = 0
        band=True
        n = int(input("valor de n: "))
        while x < n and monedero > 0 and band==True:
            color = random.randrange(1, 23)
            if (monedero-aumento)<=0 and color > 10 and color <= 20:
                band=False
                print "no hay mas dinero que apostar"
                x = x + 1
            elif monedero>=500:
                band=False
            elif color > 0 and color <= 10 and monedero<500:
                monedero = monedero + aumento
                aumento = 1
                print "gano, total: ",monedero
                x = x + 1
            elif color > 10 and color <= 20 and monedero<500:
                monedero=monedero - aumento
                print "aumento; ",aumento
                aumento = aumento * 2
                print "pierde, total= ",monedero
                x = x + 1
            elif color > 10 and color <= 20 and monedero<500:
                print "empate"
                x = x + 1

r=ruleta()
#r.jugador1()
r.jugador2()
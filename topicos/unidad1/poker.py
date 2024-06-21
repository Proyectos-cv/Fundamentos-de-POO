import numpy
import random
class pokers:
    def mano(self):
        manopalo= numpy.zeros(5)
        manocarta=numpy.zeros(5)
        corazones = numpy.zeros(14)
        picas = numpy.zeros(14)
        trebol = numpy.zeros(14)
        diamantes = numpy.zeros(14)
        for i in range(0,14):
            corazones[i] = i+1
            picas[i] = i + 1
            trebol[i] = i + 1
            diamantes[i] = i + 1
        #print diamantes
        f=0
        ronda=0
        comodin=0
        while f<5:
            palo = random.randrange(1,5)
            if palo ==1:
                carta = random.randrange(1, 15)
                if corazones[carta-1] != 0 and (carta!=14 or comodin==0):
                   if carta==14:
                       comodin=comodin+1
                   manocarta[ronda]= carta
                   manopalo[ronda]= 1
                   corazones[carta-1]=0
                   ronda=ronda+1
                   f = f + 1
            elif palo ==2:
                carta = random.randrange(1, 15)
                if picas[carta-1] != 0 and (carta!=14 or comodin==0):
                    if carta == 14:
                        comodin = comodin + 1
                    manocarta[ronda] = carta
                    manopalo[ronda] = 2
                    picas[carta-1] = 0
                    ronda = ronda + 1
                    f = f + 1
            elif palo ==3:
                carta = random.randrange(1, 15)
                if trebol[carta-1] != 0 and (carta!=14 or comodin==0):
                    if carta == 14:
                        comodin = comodin + 1
                    manocarta[ronda] = carta
                    manopalo[ronda] = 3
                    trebol[carta-1] = 0
                    ronda = ronda + 1
                    f = f + 1
            elif palo ==4:
                carta = random.randrange(1, 15)
                if diamantes[carta-1] != 0 and (carta!=14 or comodin==0):
                    if carta == 14:
                        comodin = comodin + 1
                    manocarta[ronda] = carta
                    manopalo[ronda] = 4
                    diamantes[carta-1] = 0
                    ronda = ronda + 1
                    f = f + 1

        #print""
        #print "palo 1 = corazones"
        #print "palo 2 = picas"
        #print "palo 3 = trebol"
        #print "palo 4 = diamantes"
        #print""
        #print"palo: ", manopalo
        #print "numero de la carta", manocarta
        return manopalo,manocarta,comodin

#int arre[][];
#arre=new int[2][100];
        #for j in range(1,6):
         #   if manopalo[j]==1:
          #      print manocarta[j]," de corazones"
           # elif manopalo[j]==2:
            #    print manocarta[j] , " de picas"
            #elif manopalo[j]==3:
             #   print manocarta[j] , " de trebol"
            #elif manopalo[j]==4:
             #   print manocarta[j] , " de diamantes"
        #ale= (int)100*Math.random(+100)(;)

#p=pokers()
#p.mano()


#3
#5
#1
#07
#00
#00
#000
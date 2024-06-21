import random

class component:
    def segundo(self):
        costo_tiempo=0
        costo_componente=0
        ale=random.randrange(1,101)
        print ale
        if ale > 0 and ale<=15:
            costo_tiempo=costo_tiempo+200
            costo_componente=costo_componente+800
        elif ale>15 and ale<=25:
            costo_tiempo = costo_tiempo + 200
            costo_componente = costo_componente + 800
        elif ale>25 and ale <=60:
            costo_tiempo = costo_tiempo + 200
            costo_componente = costo_componente + 800
        elif ale>60 and ale<=85:
            costo_tiempo = costo_tiempo + 200
            costo_componente = costo_componente + 800
        elif ale>85 and ale<=100:
            costo_tiempo = costo_tiempo + 200
            costo_componente = costo_componente + 800
        costo_total=costo_tiempo+costo_componente
        print costo_componente
        print costo_tiempo
        print costo_total
    def primero(self):
        costo_tiempo=0
        costo_componente=0

        num_componentes=4
        x=0
        l = []
        while x<num_componentes:
            ale = random.randrange(1, 101)
            #print ale
            if ale > 0 and ale<=15:
                horas1=500
                l.append(horas1)
            elif ale>15 and ale<=25:
                horas2 = 550
                l.append(horas2)
            elif ale>25 and ale <=60:
                horas3 = 600
                l.append(horas3)
            elif ale>60 and ale<=85:
                horas4 = 650
                l.append(horas4)
            elif ale>85 and ale<=100:
                horas5 =700
                l.append(horas5)
            x=x+1

        for i in range(len(l)):

            if l[i]==500:
                costo_componente=costo_componente+200
                costo_tiempo=costo_tiempo+100
            elif l[i]==550:
                costo_componente=costo_componente+200
                costo_tiempo=costo_tiempo+100
            elif l[i]==600:
                costo_componente=costo_componente+200
                costo_tiempo=costo_tiempo+100
            elif l[i]==650:
                costo_componente=costo_componente+200
                costo_tiempo=costo_tiempo+100
            elif l[i]==700:
                costo_componente=costo_componente+200
                costo_tiempo=costo_tiempo+100
        print l
        print costo_componente
        print costo_tiempo
        costo_total=costo_componente+costo_tiempo
        print costo_total

c=component()
#c.segundo()
c.primero()
#15 10 35 25 15
#15 25 60 85 100
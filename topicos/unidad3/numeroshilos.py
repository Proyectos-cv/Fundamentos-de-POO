import threading
import random
import time

class hil():
    def ini(self):
        t = threading.Thread(target=self.par)
        t1 = threading.Thread(target=self.impar)
        t.start()
        t1.start()
    def par(self):

        x=0

        while x<5:
            ale = random.randrange(100)
            if ale % 2 == 0:
                print "    par encontrado: "+str(ale)
                #print ale
                time.sleep(2)
                x=x+1
        #print "x",x
        print "   par termino"
    def impar(self):
        x = 0
        while x < 5:
            ale = random.randrange(100)

            if ale % 2 != 0:
                print "    impar encontrado: "+str(ale)
                #print ale
                time.sleep(2)
                x = x + 1

        #print "x",x
        print "   impar termino"

h=hil()
h.ini()

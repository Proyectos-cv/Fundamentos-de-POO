from poker import pokers
import numpy
class revisa:
    def analiza(self):
        print""
        print "palo 1 = corazones"
        print "palo 2 = picas"
        print "palo 3 = trebol"
        print "palo 4 = diamantes"
        print""
        x=0
        #uno=0
        #dos=0
        #tres=0

        itera=int(input("numero de iteraciones: "))
        band=True

        nada=float(0)
        par=float(0)
        doblepar=float(0)
        tercia=float(0)
        quintilla=float(0)
        poker=float(0)
        full=float(0)
        while x<itera and band==True:
            aux = 0
            cart = 0
            cantidad=0
            l=[]
            manopalo, manocarta, comodin=pokers().mano()
            #manocarta=numpy.array([3,4,7,5,2])
            #comodin=0
            #print comodin
           # print""
           # print manopalo
            #print manocarta
            #print""

            for i in range(0,5):
                for j in range(i+1,5):
                    if i!=j:
                        if manocarta[i]==manocarta[j] and manocarta[i] not in l:
                            l.append(manocarta[i])

            for i in range(0,5):
                aux=manocarta[i]
                for j in range(i+1,5):
                    if manocarta[j]==aux and manocarta[j]!=0:
                        #manocarta[i]=0
                        manocarta[j]=0
                        #cart=cart+1
                        cantidad=cantidad+1


            #for i in range (0,5):

            #print cantidad
            #print l

            if len(l)==1 and cantidad ==2:
                tercia=tercia+1
            elif len(l)==1 and cantidad==1:
                par=par+1
            elif len(l)==2 and cantidad==2:
                doblepar=doblepar+1
            elif len(l)==1 and cantidad==3 and comodin==1:
                quintilla=quintilla+1
            elif len(l)==2 and cantidad==3:# and comodin==1:
                full=full+1
            elif len(l)==1 and cantidad==3 and comodin==0:
                poker=poker+1

            else:
                nada=nada+1




            #print manopalo
            #print manocarta
            #print "cart: ",cart
            #print "cantidad: ", cantidad

            x=x+1
        #print l
        #print cantidad
        print""
        print"tercia: ", tercia/itera
        print"par: ", par/itera
        print"doblepar: ", doblepar/itera
        print "full: ",full/itera
        print"nada: ", nada/itera
        print"quintilla: ",quintilla/itera
        print"poker: ",poker/itera
        print""

r=revisa()
r.analiza()
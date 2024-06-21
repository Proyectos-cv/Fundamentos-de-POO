class primo:
    def prim(self,a,dato):
        cont=0
        for i in range(1,a+1):
            if a%i==0:
                cont=cont+1
        if cont<=2:
            print "numero primo: ",a
            #print"es primo"
            dato=dato+1
            return dato
        else:
            print"no es primo"
            dato=0
            return dato
    def perfecto(self):
        num=0
        nu=5
        while num<3:
            suma = 0
            for j in range(1,nu):
                if nu%j == 0:
                    suma=suma+j
            if suma==nu:
                print"numero perfecto= ", suma
                num=num+1
            nu=nu+1
    def rango(self,mayor,menor):
        a=int(input("rango menor: "))
        b = int(input("rango mayor: "))
        dato=0
        for i in range(a,b):
            dato=p.prim(i,dato)
            if dato>mayor:
                mayor =dato
            if dato<mayor and dato>menor:
                menor= dato
        print"numero mayor de primos= ", mayor
        print"numero menor de primos= ",menor
    def cantidad(self):
        menor=0
        mayor=0
        p.rango(mayor,menor)
    def menordis(self):
        dato=0
        mayor=0
        a = int(input("rango menor: "))
        b = int(input("rango mayor: "))
        for i in range(a,b):
            cont = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    cont = cont + 1
            if cont <= 2:
                print "numero primo: ", i
                # print"es primo"
                dato = 0
            else:
                print"no es primo"
                dato = dato+1
            if dato>mayor:
                mayor =dato
        print "numero mayor de no primos: ", mayor
    def formula(self):
        x=1
        bandera=True
        n=int(input("valor de n: "))
        while x<=n and bandera==True:
            dato = 0
            primo = x * x - x + 41
            dato=p.prim(primo, dato)
            if dato == 0:
                bandera=False
            x=x+1

p=primo()
#a=int(input("dame un numero: "))
#dato=0
#p.prim(a,dato)
#p.perfecto()
#mayor=0
#menor=0
#p.rango(mayor,menor)
#p.rango()
#p.cantidad()
#p.menordis()
p.formula()
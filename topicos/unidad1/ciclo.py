m=int(input("valor de m: "))
a=int(input("valor de a: "))
c=int(input("valor de c: "))
x=int(input("valor de x0: "))
aux=4
c=0
itera=((13*x)+13)%16
while c<65:
    aux=itera
    itera=((17*x)+45)%64
    x=itera
    print itera
    c=c+1

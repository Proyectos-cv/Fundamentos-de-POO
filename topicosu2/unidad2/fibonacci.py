def fibo(n):
    a,b=0,1
    while b < n:
        a, b = b, a+b
        print (b)
def factorial(n):
    num=1
    for i in range(1,n+1):
        num=num*i
    print num
def eleva(n,p):
    r=1
    for i in range(1,p+1):
        r=r*n
    print r
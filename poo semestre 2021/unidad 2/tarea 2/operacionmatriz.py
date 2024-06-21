import random as r
from mostrar import muestramatriz
class matriz:
    def __init__(self):
        print "Bienvenido a Matrices"
        self.mue=muestramatriz()
    def llenaalea(self, mat):
        for i in range(3):
            for j in range(3):
                mat[i][j] = r.randrange(1, 100)
        matd=mat
        self.mue.muestra(matd)
    def llenadiv7(self, mat):
        for i in range(3):
            j=0
            while j<3:
                s = r.randrange(1, 100)
                if s % 7 == 0:
                    mat[i][j] = s
                    j=j+1
        matd = mat
        self.mue.muestra(matd)
    def llenaprimos(self, mat):
        for i in range(3):
            j=0
            while j<3:
                conta=0
                s = r.randrange(1, 100)
                for p in range(2, s):
                    residuo = s%p
                    if residuo == 0:
                        conta = conta + 1
                if conta<2:
                    mat[i][j] = s
                    j=j+1
        matd = mat
        self.mue.muestra(matd)
    def llenaUsua(self, mat):
        for i in range(3):
            for j in range(3):
                a=int(input("que nuemro quieres colocar: "))
                mat[i][j] = a
        matd = mat
        self.mue.muestra(matd)


        # lblEti = Label(self.venPri, text="", bg="orange")
        # lblEti.grid(row=1, column=1)
        # lblEti = Label(self.venPri, font=("Arial",16),fg='blue', text="MATERIALES EL PROYECTO DE ESTRELLITA", bg="orange")
        # lblEti.place(x=400,y=25)
        # lblEti = Label(self.venPri, font=("Arial",12), fg='cyan', text= "con calidad dura más" , bg="orange")
        # lblEti.place(x=500,y=50)
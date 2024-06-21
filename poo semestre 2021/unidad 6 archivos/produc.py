#coding=utf-8
#from producto import productos
from Tkinter import *
class inven():
    def __init__(self):
        self.ventan = Toplevel()
        self.ventan.geometry("1200x1500")
        self.ventan.config(bg="orange")
        self.ventan.config(cursor="cross")
        self.ventan.config(relief="sunken")
        self.ventan.title("INVENTARIO")
        etiquta = Label(self.ventan, font=("Arial", 16), fg='blue', text="MATERIALES EL PROYECTO DE ESTRELLITA",
                       bg="orange").place(x=400, y=25)
        etiqueta = Label(self.ventan, font=("Arial", 12), fg='cyan', text="con calidad dura mas", bg="orange").place(x=500, y=50)
        etiquta=Label(self.ventan,font=("arial",10),fg='black',text="INVENTARIO",bg="orange").place(x=500 ,y=100)
        #file=open("Lista de Productos.txt","r+")
        #str= file.read(50)
        #Eti=Label(self.ventan, text=str).place(x=200,y=150)
        #file.close()
        bot=Button(self.ventan,text="consultar", bg='cyan',command=self.consultaInventario).place(x=100,y=200)
        bot=Button(self.ventan,text="actuaizar",bg='cyan',command=self.actualizacionInve).place(x=100, y=300)
        bot=Button(self.ventan,text="faltantes",bg='cyan',command=self.faltantes).place(x=100,y=400)
        bot=Button(self.ventan,text="salir",bg='cyan',command=self.volverMenu).place(x=100,y=500)
    def consultaInventario(self):
        pass
    def actualizacionInve(self):
        pass
    def faltantes(self):
        pass
    def volverMenu(self):
        self.ventan.destroy()
o=inven()
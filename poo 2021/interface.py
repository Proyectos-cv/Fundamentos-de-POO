# coding=utf-8
#from login import LoginPunto
from Tkinter import *
from inventario import inven
from empleados import trabajador
from cliente import clientes
from producto import productos
from proveedor import proveedores
import sys
class Principal:
    def ventana(self):
        #self.venPri = Tk()
        self.venPri = Toplevel()
        self.venPri.geometry("1200x1500")
        self.venPri.config(bg="orange")
        self.venPri.config(cursor="cross")
        self.venPri.config(relief="sunken")
        self.venPri.title("PRINCIPAL")

        etiqueta = Label(self.venPri, font=("Arial", 16), fg='blue', text="MATERIALES EL PROYECTO DE ESTRELLITA", bg="orange")
        etiqueta.place(x=400, y=25)
        etiqueta = Label(self.venPri, font=("Arial",12), fg='cyan', text= "con calidad dura más" , bg="orange")
        etiqueta.place(x=500, y=50)

        botonproductos = Button(self.venPri, text="Productos", bg='cyan', command=self.producto)
        botonproductos.place(x=50, y=350)
        botonproveedores = Button(self.venPri, text="Proveedores", bg='cyan', command=self.proveedor)
        botonproveedores.place(x=500, y=350)
        botonempleados = Button(self.venPri, text="Empleados", bg='cyan', command=self.trabaja)
        botonempleados.place(x=950, y=350)
        botonclientes = Button(self.venPri, text="Clientes", bg='cyan', command=self.cliente)
        botonclientes.place(x=50, y=625)
        botonventas = Button(self.venPri, text="Ventas", bg='cyan')
        botonventas.place(x=500, y=625)
        botoninventario = Button(self.venPri, text="Inventario", bg='cyan', command=self.inventario)
        botoninventario.place(x=950, y=625)
        botonsalir = Button(self.venPri, text="Salir", bg='cyan',command=self.salir)
        botonsalir.place(x=500, y=675)

        img1 = PhotoImage(file="C:\users\carlo\Downloads\imagen3.png")  # imagen1.gif, productos.gif
        widget = Label(self.venPri, image=img1)
        widget.place(x=10, y=100)
        img2 = PhotoImage(file="C:\users\carlo\Downloads\imagen4.png")  # proveedor.gif
        widget = Label(self.venPri, image=img2)
        widget.place(x=400, y=100)
        img3 = PhotoImage(file="C:\users\carlo\Downloads\imagen5.png")  # trabajador.gif   C:\users\carlo\Downloads\imagen5.png
        widget = Label(self.venPri, image=img3)
        widget.place(x=850, y=100)
        img4 = PhotoImage(file="C:\users\carlo\Downloads\imagen1.png")  # cliente.gif
        widget = Label(self.venPri, image=img4)
        widget.place(x=10, y=400)
        img5 = PhotoImage(file="C:\users\carlo\Downloads\imagen6.png")  # ventas.gif
        widget = Label(self.venPri, image=img5)
        widget.place(x=400, y=400)
        img6 = PhotoImage(file="C:\users\carlo\Downloads\imagen2.png")  # inventario.gif
        widget = Label(self.venPri, image=img6)
        widget.place(x=850, y=400)
        self.venPri.mainloop()

    def trabaja(self):
        self.l=trabajador()
    def inventario(self):
        self.k=inven()
    def cliente(self):
        self.o=clientes()
    def producto(self):
        self.d=productos()
    def proveedor(self):
        self.n=proveedores()
    def salir(self):
        exit()

# -*- coding: utf-8 -*-
# #!/usr/bin/env python
from Tkinter import *
import sys

class proveedores:
    def __init__(self):
        self.venProve =Toplevel()
        self.venProve.geometry("1200x1500")
        self.venProve.config(bg="orange")
        self.venProve.config(cursor="cross")
        self.venProve.config(relief="sunken")
        self.venProve.title("PROVEEDORES")
        lblEti = Label(self.venProve, text="", bg="orange")
        lblEti.grid(row=1, column=1)
        lblEti = Label(self.venProve, font=("Arial", 16), fg='blue', text="MATERIALES EL PROYECTO DE ESTRELLITA",bg="orange")
        lblEti.place(x=400, y=25)
        lblEti = Label(self.venProve, font=("Arial", 12), fg='cyan', text="<Con calidad dura más>", bg="orange")
        lblEti.place(x=500, y=50)
        lblEti = Label(self.venProve, font=("Arial", 12), fg='white', text="PROVEEDORES",bg='orange')
        lblEti.place(x=500, y=100)
        lblnombreProve = Label(self.venProve, text="Nombre del proveedor" , bg='orange')
        lblnombreProve.place(x=100, y=150)
        nombreProve= StringVar()
        self.cajanomProve = Entry(self.venProve, textvariable=nombreProve)
        self.cajanomProve.place(x=250, y=150)
        lbldireccionProve = Label(self.venProve, text="Direccion del proveedor", bg='orange')
        lbldireccionProve.place(x=100, y=200)
        direccionProve = StringVar()
        self.cajadireccionProve = Entry(self.venProve, textvariable=direccionProve)
        self.cajadireccionProve.place(x=250, y=200)
        lbltelefono= Label(self.venProve, text="Telefono del proveedor", bg='orange')
        lbltelefono.place(x=100, y=250)
        telefono = StringVar()
        self.cajatelefono = Entry(self.venProve, textvariable=telefono)
        self.cajatelefono.place(x=250, y=250)
        lblencargadoVentas = Label(self.venProve, text="Encargado de ventas", bg='orange')
        lblencargadoVentas.place(x=100, y=300)
        encargadoVentas = StringVar()
        self.cajaencargadoVentas = Entry(self.venProve, textvariable=encargadoVentas)
        self.cajaencargadoVentas.place(x=250, y=300)
        lbltipo = Label(self.venProve, text="Tipos de productos", bg='orange')
        lbltipo.place(x=100, y=350)
        tipo = StringVar()
        self.cajatipo= Entry(self.venProve, textvariable=tipo)
        self.cajatipo.place(x=250, y=350)
        btnagregarprove = Button(self.venProve, text="Guardar", bg='cyan', command=self.agregarProve)
        btnagregarprove.place(x=400, y=450)
        btneliminarprove = Button(self.venProve, text="Eliminar", bg='cyan', command=self.bajaProve)
        btneliminarprove.place(x=550, y=450)
        btnactualizarprove = Button(self.venProve, text="Actualizar", bg='cyan', command=self.actualizacionProve)
        btnactualizarprove.place(x=700, y=450)
        btnmandarPedido = Button(self.venProve, text="Mandar Pedido", bg='cyan', command=self.actualizacionProve)
        btnmandarPedido.place(x=850, y=450)
        btnvolver = Button(self.venProve, text="Volver", bg='cyan', command=self.volverMenu)
        btnvolver.place(x=1000, y=450)
        #proveedor = PhotoImage(file="proveedor.gif")
        #widget = Label(self.venProve, image=proveedor)
        #widget.place(x=800, y=200)
        self.venProve.mainloop()


    def agregarProve(self):
        pass
    def bajaProve(self):
        pass
    def actualizacionProve(self):
        pass
    def mandarPedido(self):
        pass
    def volverMenu(self):
        self.venProve.withdraw()
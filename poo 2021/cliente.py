# -*- coding: utf-8 -*-�
# #!/usr/bin/env python
from Tkinter import *

class clientes:
    def __init__(self):
        self.venClien =Toplevel()
        self.venClien.geometry("1200x1500")
        self.venClien.config(bg="orange")
        self.venClien.config(cursor="cross")
        self.venClien.config(relief="sunken")
        self.venClien.title("Clientes")
        #self.venClien.iconbitmap("Icono.ico")

        lblEti = Label(self.venClien, text="", bg="orange")
        lblEti.grid(row=1, column=1)
        lblEti = Label(self.venClien, font=("Arial", 16), fg='blue', text="MATERIALES EL PROYECTO DE ESTRELLITA",bg="orange")
        lblEti.place(x=400, y=25)
        lblEti = Label(self.venClien, font=("Arial", 12), fg='cyan', text="<Con calidad dura más>", bg="orange")
        lblEti.place(x=500, y=50)
        lblEti = Label(self.venClien, font=("Arial", 12), fg='white', text="CLIENTES",bg='orange')
        lblEti.place(x=500, y=100)

        lblnombreClien = Label(self.venClien, text="Nombre del Cliente" , bg='orange')
        lblnombreClien.place(x=100, y=150)
        nombreclien= StringVar()
        self.cajanomclien = Entry(self.venClien, textvariable=nombreclien)
        self.cajanomclien.place(x=250, y=150)
        lblcorreoclien = Label(self.venClien, text="Correo del cliente", bg='orange')
        lblcorreoclien.place(x=100, y=200)
        correoclien = StringVar()
        self.cajacorreoclien = Entry(self.venClien, textvariable=correoclien)
        self.cajacorreoclien.place(x=250, y=200)
        lbltelclien = Label(self.venClien, text="Telefono del cliente", bg='orange')
        lbltelclien.place(x=100, y=250)
        telclien = StringVar()
        self.cajatelclien = Entry(self.venClien, textvariable=telclien)
        self.cajatelclien.place(x=250, y=250)
        lblocupacion = Label(self.venClien, text="Ocupacion", bg='orange')
        lblocupacion.place(x=100, y=300)
        ocupacion = StringVar()
        self.cajaocupacion = Entry(self.venClien, textvariable=ocupacion)
        self.cajaocupacion.place(x=250, y=300)
        lbltipo = Label(self.venClien, text="Cliente frecuente s/n", bg='orange')
        lbltipo.place(x=100, y=350)
        tipo = StringVar()
        self.cajatipo= Entry(self.venClien, textvariable=tipo)
        self.cajatipo.place(x=250, y=350)
        btnagregarclien = Button(self.venClien, text="Guardar", bg='cyan', command=self.agregarCliente)
        btnagregarclien.place(x=500, y=450)
        btneliminarclien = Button(self.venClien, text="Eliminar", bg='cyan', command=self.bajaCliente)
        btneliminarclien.place(x=650, y=450)
        btnactualizarclien = Button(self.venClien, text="Actualizar", bg='cyan', command=self.actualizacionCliente)
        btnactualizarclien.place(x=800, y=450)
        btnvolver = Button(self.venClien, text="Volver", bg='cyan', command=self.volverMenu)
        btnvolver.place(x=950, y=450)
        #cliente = PhotoImage(file="cliente.gif")
        #widget = Label(self.venClien, image=cliente)
        #widget.place(x=800, y=200)
        self.venClien.mainloop()

    def agregarCliente(self):
        pass
    def bajaCliente(self):
        pass
    def actualizacionCliente(self):
        pass
    def publicidad(self):
        pass
    def regFrecuencia(self):
        pass
    def volverMenu(self):
        self.venClien.withdraw()
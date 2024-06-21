# -*- coding: utf-8 -*-�
# #!/usr/bin/env python
from Tkinter import *
#from Datos import DatosComunes
#from Interface import Funciones
from excepciones import EspacioBlanco, Negativos, ECorreo, ETelefono
class Proveedores():
#class Proveedores(DatosComunes, Funciones):
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
        self.nombreProve= StringVar()
        self.cajanomProve = Entry(self.venProve, textvariable=self.nombreProve)
        self.cajanomProve.place(x=250, y=150)
        lbldireccionProve = Label(self.venProve, text="Direccion del proveedor", bg='orange')
        lbldireccionProve.place(x=100, y=200)
        self.direccionProve = StringVar()
        self.cajadireccionProve = Entry(self.venProve, textvariable=self.direccionProve)
        self.cajadireccionProve.place(x=250, y=200)
        lbltelefono= Label(self.venProve, text="Telefono del proveedor", bg='orange')
        lbltelefono.place(x=100, y=250)
        self.telefono = StringVar()
        self.cajatelefono = Entry(self.venProve, textvariable=self.telefono)
        self.cajatelefono.place(x=250, y=250)
        lblencargadoVentas = Label(self.venProve, text="Encargado de ventas", bg='orange')
        lblencargadoVentas.place(x=100, y=300)
        self.encargadoVentas = StringVar()
        self.cajaencargadoVentas = Entry(self.venProve, textvariable=self.encargadoVentas)
        self.cajaencargadoVentas.place(x=250, y=300)
        lbltipo = Label(self.venProve, text="Tipos de productos", bg='orange')
        lbltipo.place(x=100, y=350)
        self.tipo = StringVar()
        self.cajatipo= Entry(self.venProve, textvariable=self.tipo)
        self.cajatipo.place(x=250, y=350)
        btnagregarprove = Button(self.venProve, text="Guardar", bg='cyan', command=self.guardar)
        btnagregarprove.place(x=400, y=450)
        btneliminarprove = Button(self.venProve, text="Eliminar", bg='cyan', command=self.baja)
        btneliminarprove.place(x=550, y=450)
        btnactualizarprove = Button(self.venProve, text="Actualizar", bg='cyan', command=self.actualizacionProve)
        btnactualizarprove.place(x=700, y=450)
        btnmandarPedido = Button(self.venProve, text="Mandar Pedido", bg='cyan', command=self.actualizacionProve)
        btnmandarPedido.place(x=850, y=450)
        btnvolver = Button(self.venProve, text="Volver", bg='cyan', command=self.volverMenu)
        btnvolver.place(x=1000, y=450)
        #proveedor = PhotoImage(file="proveedor.gif")
        widget = Label(self.venProve, image=proveedor)
        widget.place(x=800, y=200)
        self.venProve.mainloop()

    def guardar(self):
        try:
            self.nomProveedor=self.nombreProve.get()
            if self.nomProveedor=="":
                raise EspacioBlanco
            self.dicProveedor=self.direccionProve.get()
            if self.dicProveedor=="":
                raise EspacioBlanco
            self.telProveedor=self.telefono.get()
            if self.telProveedor=="":
                raise EspacioBlanco
            long = len(self.telProveedor)
            if long != 10:
                raise ETelefono
            self.encargadoventas=self.encargadoVentas.get()
            if self.encargadoventas=="":
                raise EspacioBlanco
            self.tipo=self.tipo.get()
            if self.tipo=="":
                raise EspacioBlanco
            Lista_Proveedores = open("Lista de Proveedores.txt", 'a')
            Lista_Proveedores.write("   ")
            Lista_Proveedores.write(self.nomProveedor)
            Lista_Proveedores.write("    ")
            Lista_Proveedores.write(self.dicProveedor)
            Lista_Proveedores.write("           ")
            Lista_Proveedores.write(self.telProveedor)
            Lista_Proveedores.write("            ")
            Lista_Proveedores.write(self.encargadoventas)
            Lista_Proveedores.write("         ")
            Lista_Proveedores.write(self.tipo)
            Lista_Proveedores.write("\n")
            Lista_Proveedores.close()
            self.agregar()
        except EspacioBlanco as e:
            pass
        except ECorreo as e:
            pass
        except ETelefono as e:
            pass
    def eliminar(self):
        print "si elimino"
        self.venGua.destroy()
    def actualizacionProve(self):
        pass
    def mandarPedido(self):
        pass
    def volverMenu(self):
        self.venProve.withdraw()
    def baja(self):
        self.venGua = Tk()
        self.venGua.iconbitmap("Icono.ico")
        self.venGua.geometry("300x100")
        self.venGua.config(bg="orange")
        self.venGua.title("Remover")
        anuncioQuitar = Label(self.venGua, text="Removido con exito", fg="navy", bg="orange", font=("Arial", 15))
        anuncioQuitar.place(x=30, y=0)
        btnInicio = Button(self.venGua, text="Cancelar", bg='cyan', command=self.cerrar)
        btnInicio.place(x=50, y=50)
        btnInicio = Button(self.venGua, text="OK", bg='cyan', command=self.eliminar)
        btnInicio.place(x=150, y=50)
        self.venGua.mainloop()
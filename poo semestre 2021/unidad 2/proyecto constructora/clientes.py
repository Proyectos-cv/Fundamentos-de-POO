# -*- coding: utf-8 -*-�
# #!/usr/bin/env python
from Tkinter import *
#from Datos import DatosComunes
#from Interface import Funciones
from excepciones import EspacioBlanco, Negativos, ClienteF, ECorreo, ETelefono
class Cliente():
#class Cliente(DatosComunes, Funciones):
    def __init__(self):
        self.venClien =Toplevel()
        self.venClien.geometry("1200x1500")
        self.venClien.config(bg="orange")
        self.venClien.config(cursor="cross")
        self.venClien.config(relief="sunken")
        self.venClien.title("Clientes")
        self.venClien.iconbitmap("Icono.ico")
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
        self.nombreclien= StringVar()
        self.cajanomclien = Entry(self.venClien, textvariable=self.nombreclien)
        self.cajanomclien.place(x=250, y=150)
        lblcorreoclien = Label(self.venClien, text="Correo del cliente", bg='orange')
        lblcorreoclien.place(x=100, y=200)
        self.correoclien = StringVar()
        self.cajacorreoclien = Entry(self.venClien, textvariable=self.correoclien)
        self.cajacorreoclien.place(x=250, y=200)
        lbltelclien = Label(self.venClien, text="Telefono del cliente", bg='orange')
        lbltelclien.place(x=100, y=250)
        self.telclien = StringVar()
        self.cajatelclien = Entry(self.venClien, textvariable=self.telclien)
        self.cajatelclien.place(x=250, y=250)
        lblocupacion = Label(self.venClien, text="Ocupacion", bg='orange')
        lblocupacion.place(x=100, y=300)
        self.ocupacion = StringVar()
        self.cajaocupacion = Entry(self.venClien, textvariable=self.ocupacion)
        self.cajaocupacion.place(x=250, y=300)
        lbltipo = Label(self.venClien, text="Cliente frecuente s/n", bg='orange')
        lbltipo.place(x=100, y=350)
        self.tipo = StringVar()
        self.cajatipo= Entry(self.venClien, textvariable=self.tipo)
        self.cajatipo.place(x=250, y=350)
        btnagregarclien = Button(self.venClien, text="Guardar", bg='cyan', command=self.guardar)
        btnagregarclien.place(x=500, y=450)
        btneliminarclien = Button(self.venClien, text="Eliminar", bg='cyan', command=self.baja)
        btneliminarclien.place(x=650, y=450)
        btnactualizarclien = Button(self.venClien, text="Actualizar", bg='cyan', command=self.actualizacionCliente)
        btnactualizarclien.place(x=800, y=450)
        btnvolver = Button(self.venClien, text="Volver", bg='cyan', command=self.volverMenu)
        btnvolver.place(x=950, y=450)
        cliente = PhotoImage(file="cliente.gif")
        widget = Label(self.venClien, image=cliente)
        widget.place(x=800, y=200)
        self.venClien.mainloop()
    def guardar(self):
        try:
            self.nomCliente=self.nombreclien.get()
            if self.nomCliente=="":
                raise EspacioBlanco
            self.correoCliente=self.correoclien.get()
            if self.correoCliente=="":
                raise EspacioBlanco
            arroba=False
            longcor=len(self.correoCliente)
            s=0
            while s<longcor:
                m=self.correoCliente[s]
                if m=='@':
                   arroba=True
                s=s+1
            if arroba==False:
                raise ECorreo
            self.telCliente=self.telclien.get()
            if self.telCliente=="":
                raise EspacioBlanco
            long=len(self.telCliente)
            if long!=10:
                raise ETelefono
            self.ocupaCliente=self.ocupacion.get()
            if self.ocupaCliente=="":
                raise EspacioBlanco
            self.tipoCliente=self.tipo.get()
            if self.tipoCliente=="":
                raise EspacioBlanco
            elif self.tipoCliente!='n' and self.tipoCliente!='s':
                raise ClienteF
            #Lista_Clientes = open("Lista de Clientes.txt", 'a')
            #Lista_Clientes.write("   ")
            #Lista_Clientes.write(self.nomCliente)
            #Lista_Clientes.write("    ")
            #Lista_Clientes.write(self.correoCliente)
            #Lista_Clientes.write("           ")
            #Lista_Clientes.write(self.telCliente)
            #Lista_Clientes.write("            ")
            #Lista_Clientes.write(self.ocupaCliente)
            #Lista_Clientes.write("         ")
            #Lista_Clientes.write(self.tipoCliente)
            #Lista_Clientes.write("\n")
            #Lista_Clientes.close()
            self.agregar()
        except EspacioBlanco as e:
            pass
        except ClienteF as e:
            print "error"
        except ECorreo as e:
            pass
        except ETelefono as e:
            pass
    def eliminar(self):
        print "si elimino"
        self.venGua.destroy()
    def actualizacionCliente(self):
        pass
    def publicidad(self):
        pass
    def regFrecuencia(self):
        pass
    def volverMenu(self):
        self.venClien.withdraw()
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
#c=Cliente()
#c.guardar()
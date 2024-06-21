#coding=utf-8
#from Producto import Productos
from Tkinter import *
class inven():
    def __init__(self):
        self.ventan=Tk()
        self.ventan = Toplevel()
        self.ventan.geometry("1200x1500")
        self.ventan.config(bg="orange")
        self.ventan.config(cursor="cross")
        self.ventan.config(relief="sunken")
        self.ventan.title("INVENTARIO")
        #texto1 = Entry(self.ventan).place(x=300, y=200,textvariable=usuario)

        #texto1.grid(row=5, column=7)
        etiqueta = Label(self.ventan, font=("Arial", 16), fg='blue', text="MATERIALES EL PROYECTO DE ESTRELLITA",
                       bg="orange").place(x=400, y=25)
        etiqueta = Label(self.ventan, font=("Arial", 12), fg='cyan', text="con calidad dura mas", bg="orange").place(x=500, y=50)
        etiqueta=Label(self.ventan,font=("arial",10),fg='black',text="INVENTARIO",bg="orange").place(x=500 ,y=100)

        bot=Button(self.ventan,text="consultar", bg='cyan',command=self.consultaInventario).place(x=100,y=200)
        bot=Button(self.ventan,text="actuaizar",bg='cyan',command=self.actualizacionInve).place(x=100, y=300)
        bot=Button(self.ventan,text="faltantes",bg='cyan',command=self.faltantes).place(x=100,y=400)
        bot=Button(self.ventan,text="salir",bg='cyan',command=self.volverMenu).place(x=100,y=500)

        #print "GUARDANDO UN REGISTRO"
        #file = open("myFile.txt", "a")
        #clave = int(input("Dame la clave del producto: "))
        #prod = raw_input("Dame el nombre del producto: ")
        #preciouni = float(input("Dame el precio del producto: "))
        #producto = str(clave) + "                 " + prod + "                 " + str(preciouni) + "\n"
        #file.write(producto)
        #print "Datos escritos en el archivo"
        #file.close()

        #print file.closed
        #file = open("myFile.txt", "r+")
        #st = file.read(1000)
        #etiquta = Label(self.ventan, font=("Arial", 12), fg='blue', text=st,
         #               bg="orange").place(x=400, y=200)
        #file.close()
        #print file.closed

        file=open("myFile.txt", "r+")
        l=[]
        leer= file.readlines()
        for i in leer:
            l.append(i)
            l=i.replace("4","5")
        print l
        file.close()
        print file.closed
        self.ventan.mainloop()
    def crear(self):
        file = open("myFile.txt", "w")
        #creamos el archivo
        producto = str("clave") + "     " + "prod" + "     " + str("preciounitario") + "\n"
        file.write(producto)
        print "El archivo esta creado"
        file.close()
    def guardarDatos(self):
        print "GUARDANDO UN REGISTROdef consultaInventario(self):
        pass
    def actualizacionInve(self):
        pass
    def faltantes(self):
        pass
    def volverMenu(self):
        self.ventan.destroy()"
        file = open("myFile.txt", "a")
        clave=int(input("Dame la clave del producto: "))
        prod=raw_input("Dame el nombre del producto: ")
        preciouni=float(input("Dame el precio del producto: "))
        producto=str(clave)+"     "+prod+"     "+str(preciouni)+"\n"
        file.write(producto)
        print "Datos escritos en el archivo"
        file.close()

o=inven()
#o.crear()
#o.crear()
#o.guardarDatos()

class NewFile:
    def __init__(self):
        print "Creando el archivo"
    def crear(self):
        file = open("myFile.txt", "w")
        #creamos el archivo
        print "El archivo esta creado"
        file.close()
    def guardarDatos(self):
        print "GUARDANDO UN REGISTRO"
        file = open("myFile.txt", "a")
        clave=int(input("Dame la clave del producto: "))
        prod=raw_input("Dame el nombre del producto: ")
        preciouni=float(input("Dame el precio del producto: "))
        producto=str(clave)+"     "+prod+"     "+str(preciouni)+"\n"
        file.write(producto)
        print "Datos escritos en el archivo"
        file.close()
    def leyendoDatos(self):
        file = open("myFile.txt", "r+")
        str = file.read(50)
        print "Lo que tenemos en el archivo es : ", str
        file.close()
    def leyendoLineas(self):
        print "INVENTARIO DE PRODUCTOS"
        with open("myFile.txt", "r") as f:
            read_data=f.read()
            print read_data
            f.close()
    def consulta(self, buscar):
        self.dato=buscar
        print "BUSCANDO UN REGISTRO"
        encontrado = False
        for linea in open("myFile.txt", "r"):
            linea = linea.strip()  # El strip elimina espacios
            clave, nomprod, precio = linea.split()
            if self.dato == nomprod:
                self.c = clave
                self.np = nomprod
                self.p = precio
                self.cambia = str(self.c) + "     " + self.np + "     " + str(self.p)
                encontrado = True
        if encontrado == True:
            print "CLAVE: ", self.c
            print "PRODUCTO: ", self.np
            print "PRECIO UNITARIO: ", self.p
        else:
            print "Producto no encontrado"
    def actualiza(self):
        print "MODIFICANDO UN REGISTRO"
        modifica = False  # Ponemos una bandera para saber si actualizamos el registro
        # abrimos el archivo solo de lectura
        f = open("myFile.txt", "r")
        # Creamos una lista con cada una de sus lineas
        lineas = f.readlines()
        # cerramos el archivo
        f.close()
        buscar = raw_input("Dame el nombre del productoa modificar: ")
        self.consulta(buscar)
        f = open("myFile.txt", "w")
        # recorremos todas las lineas
        for linea in lineas:
            # agregamos al final \n que es el salto de linea
            if linea != self.cambia + "\n":
                f.write(linea)
                # print "Registro libre"
            else:
                print "Encontrado"
                print "Dame los nuevos datos, pero la clave no puedes modificarla"
                prodM = raw_input("Dame el nombre del producto: ")
                preciouniM = float(input("Dame el precio del producto: "))
                modifica = True
                productoM = str(self.c) + "     " + prodM + "     " + str(preciouniM) + "\n"
                f.write(productoM)
        # cerramos el archivo
        f.close()
        if modifica == True:
            print "Registro modificado"


  #archi=NewFile()
#archi.crear()
#archi.guardarDatos()
#archi.leyendoDatos()
  #archi.leyendoLineas()
#archi.consulta()
  #archi.actualiza()
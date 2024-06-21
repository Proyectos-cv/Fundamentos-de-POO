from Tkinter import *
class nuevo():
    #def busca(self):
        #buscar = raw_input("dato a buscar")
    #def consultaProducto(self, buscar):
    def consultaProducto(self):
        buscar = raw_input("dato a buscar")
        self.dato = buscar
        print "BUSCANDO UN REGISTRO"
        encontrado = False
        for linea in open("miarchivo.txt", "r"):
            linea = linea.strip()  # El strip elimina espacios
            clave, nomprod,cantidad, marca, precio, precio1,caducidad = linea.split()
            if self.dato == clave:
                self.c = clave
                self.np = nomprod
                self.can=cantidad
                self.mar=marca
                self.p = precio
                self.pr=precio1
                self.cau=caducidad
                self.cambia = str(self.c) + "     " + self.np +  "     " + str(self.can) + "     " +  self.mar +  "     " + str(self.p)+ "     " + str(self.pr)+ "     " +  self.cau
                encontrado = True
        if encontrado == True:
            print "CLAVE: ", self.c
            print "PRODUCTO: ", self.np
            print "PRECIO UNITARIO: ", self.p
            print "CANTIDAD: ", self.can
        else:
            self.winequi = Toplevel()
            self.winequi.iconbitmap("Icono.ico")
            self.winequi.geometry("425x100")
            self.winequi.config(bg="orange")
            self.winequi.title("ALERTA")
            anuncioCorre2 = Label(self.winequi, text="PRODUCTO NO ENCONTRADO", fg="navy",bg="orange",font=("Arial", 15))
            anuncioCorre2.place(x=2, y=25)
            btnInicio = Button(self.winequi, text="Okay", bg='cyan', command=self.close_window)
            btnInicio.place(x=200, y=(75))
    def actualizacionProducto(self):
        print "MODIFICANDO UN REGISTRO"
        modifica = False  # Ponemos una bandera para saber si actualizamos el registro
        # abrimos el archivo solo de lectura
        f = open("miarchivo.txt", "r")
        # Creamos una lista con cada una de sus lineas
        lineas = f.readlines()
        # cerramos el archivo
        f.close()
        #bus= self.codigo.get()
        #buscar=str(bus)
        #self.consultaProducto(buscar)
        f = open("miarchivo.txt", "w")
        # recorremos todas las lineas
        for linea in lineas:
            # agregamos al final \n que es el salto de linea
            if linea != self.cambia + "\n":
                f.write(linea)
            #    print "Registro libre"
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
            self.winequi = Toplevel()
            self.winequi.iconbitmap("Icono.ico")
            self.winequi.geometry("425x100")
            self.winequi.config(bg="orange")
            self.winequi.title("NOTIFICA")
            anuncioCorre2 = Label(self.winequi, text="REGISTRO MMODIFICADO", fg="navy",bg="orange",font=("Arial", 15))
            anuncioCorre2.place(x=2, y=25)
            btnInicio = Button(self.winequi, text="Okay", bg='cyan', command=self.close_window)
            btnInicio.place(x=200, y=(75))
    def close_window(self):
        print"aqui"
f=nuevo()
f.consultaProducto()
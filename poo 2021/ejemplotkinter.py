from Tkinter import *
class PrincipalInterfaz:
    def __init__(self):
        self.winPrinci = Toplevel()
        self.winPrinci.geometry("1600x800")
        self.winPrinci.title('BIENVENIDOS A ABARROTES PATITO')
        self.winPrinci.config(bg="blue")
        lblTitulo = Label(self.winPrinci, bg="pink", width=50, text="ABARROTES PATITO",
                relief="solid", borderwidth=0)
        lblTitulo.place(x=200, y=50)
        btnProductos = Button(self.winPrinci, text="PRODUCTOS", command=self.productos)
        btnProductos.place(x=250, y=130)
        btnProveedores = Button(self.winPrinci, text="PROVEEDORES", command=self.proveedor)
        btnProveedores.place(x=250, y=180)
        btnVentas = Button(self.winPrinci, text="VENTAS", command=self.ventas)
        btnVentas.place(x=250, y=230)
        # Insertando una imagen en la ventana
        #img = PhotoImage(file="user.gif")
        #widget = Label(self.winPrinci, image=img)
        #widget.place(x=780, y=120)
        self.winPrinci.mainloop()
    def productos(self):
        print "Llamada a ventana de productos"
    def proveedor(self):
        print "Llamada a ventana de proveedores"
    def ventas(self):
        print "Llamada a ventana de ventas"
p=PrincipalInterfaz()
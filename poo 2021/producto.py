# -*- coding: utf-8 -*-
# #!/usr/bin/env python
from Tkinter import *
import sys
#from Proveedor import Proveedores
#from falla import error1
class productos:
    def __init__(self):
        self.venProdu =Toplevel()
        self.venProdu.geometry("1200x1500")
        self.venProdu.config(bg="orange")
        self.venProdu.config(cursor="cross")
        self.venProdu.config(relief="sunken")
        self.venProdu.title("PRODUCTOS")

        lblEti = Label(self.venProdu, text="", bg="orange")
        lblEti.grid(row=1, column=1)
        lblEti = Label(self.venProdu, font=("Arial", 16), fg='blue', text="MATERIALES EL PROYECTO DE ESTRELLITA",bg="orange")
        lblEti.place(x=400, y=25)
        lblEti = Label(self.venProdu, font=("Arial", 12), fg='cyan', text="<Con calidad dura más>", bg="orange")
        lblEti.place(x=500, y=50)
        lblEti = Label(self.venProdu, font=("Arial", 12), fg='white', text="PRODUCTOS", bg="orange")
        lblEti.place(x=500, y=100)
        lblnombreProducto = Label(self.venProdu, text="Nombre del producto", bg='orange')
        lblnombreProducto.place(x=100, y=150)
        nombreProducto = StringVar()
        self.cajanomProducto = Entry(self.venProdu, textvariable=nombreProducto)
        self.cajanomProducto.place(x=250, y=150)
        lblPrecioCompraProducto = Label(self.venProdu, text="Precio de compra", bg='orange')
        lblPrecioCompraProducto.place(x=100, y=200)
        PrecioCompraProducto = DoubleVar()
        self.cajaPrecioCompraProducto = Entry(self.venProdu, textvariable=PrecioCompraProducto)
        self.cajaPrecioCompraProducto.place(x=250, y=200)
        lblprecioVentaProducto = Label(self.venProdu, text="Precio de venta", bg='orange')
        lblprecioVentaProducto.place(x=100, y=250)
        lblprecioVentaProducto = DoubleVar()
        self.cajaprecioVentaProducto = Entry(self.venProdu, textvariable=lblprecioVentaProducto)
        self.cajaprecioVentaProducto.place(x=250, y=250)
        lblmarca = Label(self.venProdu, text="Marca", bg='orange')
        lblmarca.place(x=100, y=300)
        marca = StringVar()
        self.cajamarca = Entry(self.venProdu, textvariable=marca)
        self.cajamarca.place(x=250, y=300)
        lblcantidad = Label(self.venProdu, text="Cantidad", bg='orange')
        lblcantidad.place(x=100, y=350)
        cantidad= IntVar()
        self.cajacantidad = Entry(self.venProdu, textvariable=cantidad)
        self.cajacantidad.place(x=250, y=350)
        lblcodigo = Label(self.venProdu, text="Codigo", bg='orange')
        lblcodigo.place(x=100, y=400)
        codigo = IntVar()
        self.cajacodigo = Entry(self.venProdu, textvariable=codigo)
        self.cajacodigo.place(x=250, y=400)
        lbldescripcionProducto = Label(self.venProdu, text="Descripcion", bg='orange')
        lbldescripcionProducto.place(x=100, y=450)
        descripcionProducto= StringVar()
        self.cajadescripcionProducto = Entry(self.venProdu, textvariable=descripcionProducto)
        self.cajadescripcionProducto.place(x=250, y=450)
        lblfechaCaducidad= Label(self.venProdu, text="Fecha caducidad", bg='orange')
        lblfechaCaducidad.place(x=100, y=500)
        fechaCaducidad = IntVar()
        self.cajafechaCaducidad = Entry(self.venProdu, textvariable=fechaCaducidad)
        self.cajafechaCaducidad.place(x=250, y=500)
        btnagregar = Button(self.venProdu, text="Guardar", bg='cyan', command=self.agregarProducto)
        btnagregar.place(x=500, y=600)
        btneliminar = Button(self.venProdu, text="Eliminar", bg='cyan', command=self.bajaProducto)
        btneliminar.place(x=600, y=600)
        btnactualizar = Button(self.venProdu, text="Actualizar", bg='cyan', command=self.actualizacionProducto)
        btnactualizar.place(x=700, y=600)
        btnreportemal = Button(self.venProdu, text="Reporte de mal estado", bg='cyan', command=self.reportarMalEdo)
        btnreportemal.place(x=800, y=600)
        btnsalir = Button(self.venProdu, text="Hacer Pedidos", bg='cyan', command=self.hacerPedido)
        btnsalir.place(x=950, y=600)
        btnsalir = Button(self.venProdu, text="Volver", bg='cyan', command=self.volverMenu)
        btnsalir.place(x=1050, y=600)
        #productos = PhotoImage(file="productos.gif")
        #widget = Label(self.venProdu, image=productos)
        #widget.place(x=800, y=200)
        self.venProdu.mainloop()
        #try:
            #if self.cajacantidad:
            #if self.cajacantidad==0:
               #raise error1
        #except error1:
            #print error1

    def agregarProducto(self):
        pass
    def bajaProducto(self):
        pass
    def actualizacionProducto(self):
        pass
    def reportarMalEdo(self):
        pass
    def hacerPedido(self):
        pass
    def volverMenu(self):
        self.venProdu.withdraw()
e=productos()
e.productos()
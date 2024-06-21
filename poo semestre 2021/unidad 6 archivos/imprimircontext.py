from Tkinter import *
import Tkinter as tk
class inven():
    def __init__(self):
        self.ventan=Tk()
        self.ventan = Toplevel()
        self.ventan.geometry("1200x1500")
        self.ventan.config(bg="orange")
        self.ventan.config(cursor="cross")
        self.ventan.config(relief="sunken")
        self.ventan.title("INVENTARIO")

        etiqueta = Label(self.ventan, font=("Arial", 16), fg='blue', text="MATERIALES EL PROYECTO DE ESTRELLITA",
                       bg="orange").place(x=400, y=25)
        etiqueta = Label(self.ventan, font=("Arial", 12), fg='cyan', text="con calidad dura mas", bg="orange").place(x=500, y=50)
        etiqueta=Label(self.ventan,font=("arial",10),fg='black',text="INVENTARIO",bg="orange").place(x=500 ,y=100)

        bot=Button(self.ventan,text="consultar", bg='cyan',command=self.consultaInventario).place(x=100,y=200)
        bot=Button(self.ventan,text="actuaizar",bg='cyan',command=self.actualizacionInve).place(x=100, y=300)
        bot=Button(self.ventan,text="faltantes",bg='cyan',command=self.faltantes).place(x=100,y=400)
        bot=Button(self.ventan,text="salir",bg='cyan',command=self.volverMenu).place(x=100,y=500)

        # winInv = Tk()
        texto = Text(self.ventan)
        texto.place(x=250, y=200)
        scroll=tk.Scrollbar(self.ventan, command=texto.yview)
        texto.configure(yscrollcommand=scroll.set)
        # text=tk.Text(self.ventan, height=10, width=30)
        # scroll.pack(side=tk.RIGHT, fill=tk.Y)
        # scroll = tk.Scrollbar(winInv, command=texto.yview)
        # texto.configure(yscrollcommand=scroll.set)
        texto.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        texto.tag_configure('big', font=('Verdana', 20, 'bold'))
        texto.tag_configure('color',
                            foreground='#476042',
                            font=('Tempus Sans ITC', 12, 'bold'))
        espacio = "\t\t\t"
        for linea in open("myFile.txt", "r"):
            linea = linea.strip()
            clave, nomprod, precio = linea.split()
            texto.insert('insert', "\t")
            texto.insert('insert', clave, 'color')
            texto.insert('insert', espacio)
            texto.insert('insert', nomprod, 'color')
            texto.insert('insert', espacio)
            texto.insert('insert', "\t")
            texto.insert('insert', precio, 'color')
            texto.insert('insert', "\n")
        texto.configure(state='disabled')
        self.ventan.mainloop()


        else:
        clave, nomprod, precioc, preciov, marca, cantidad, caducidad = linea.split()
        print nomprod
        Codigo = str(self.codigo.get())
        NombreProducto = self.nombreProducto.get()
        if NombreProducto == "":
            NombreProducto = nomprod
        Cantidad = (self.cantidad.get())
        Cantidad = str(Cantidad)
        if Cantidad == "0":
            Cantidad = cantidad
        Marca = self.marca.get()
        if Marca == "":
            Marca = marca


    def consultaInventario(self):
       pass

    def actualizacionInve(self):
        pass

    def faltantes(self):
        pass

    def volverMenu(self):
        # self.ventan.destroy()
        pass
o=inven()



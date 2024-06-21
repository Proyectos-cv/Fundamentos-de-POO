class NewFile:
    def __init__(self):
        print "Creando el archivo"
    def crear(self):
        file = open("myFile.txt", "w")
        #creamos el archivo
        print "El archivo esta creado"
        file.close()

    def guardarDatos(self):
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
        with open("myFile.txt", "r") as f:
            read_data=f.read()
            print read_data
            f.close()

archi=NewFile()
#archi.crear()
archi.guardarDatos()
archi.leyendoDatos()
archi.leyendoLineas()
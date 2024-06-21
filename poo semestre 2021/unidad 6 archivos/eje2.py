class TrabajoArchivos:
    def __init__(self):
        print "Trabajando con archivos"
    def atributosArchivos(self):
        #creamos el archivo
        file = open("miarchivo.txt", "w")
        #con este atributo nos da el nombre
        print "Nombre del archivo : ", file.name
        # Con este atributo nos dice si esta cerrado
        print "Cerrado o no : ", file.closed
        #Con esto nos dice en que modo esta el archivo
        print "Modo de apertura : ", file.mode
        #Con esto se cierra el archivo
        file.close()
        # Volvemos a preguntar si esta cerrado
        print "Cerrado o no : ", file.closed

    def escribirArchi(self):
        # Con este ejemplo agregamos informacion al archivo
        file = open("miarchivo.txt", "w")
        file.write("Este es mi primer archivo \n en Python, y espero aprender mucho \n de ellos")
        file.close()
        print "Cerrado o no : ", file.closed

    def leyendoArchi(self):
        file = open("miarchivo.txt", "r+")
        str = file.read(70)
        print "Lo que tenemos en el archivo es : ", str
        file.close()
        print "Cerrado o no : ", file.closed


archi = TrabajoArchivos()
archi.atributosArchivos()
archi.escribirArchi()
archi.leyendoArchi()


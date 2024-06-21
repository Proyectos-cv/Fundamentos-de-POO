#file = open("guarda.txt", "w")
#print "El archivo esta creado"
#file.close()

def guard(c):
    file = open("guarda.txt", "a")
    clave = c
    producto = (str(c)+" , " + "\n")
    file.write(producto)
    file.close()
def muestra():
    file = open("guarda.txt", "r+")
    str = file.read(50)
    #print "Lo que tenemos en el archivo es : ", str
    file.close()
    return str
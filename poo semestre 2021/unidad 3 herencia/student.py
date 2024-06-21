from person import personas
class estudiantes (personas):
    def __init__(self):
        print "clase estudiante"
    def promedio(self, c1, c2, c3):
        r=(c1+c2+c3)/3
        print r

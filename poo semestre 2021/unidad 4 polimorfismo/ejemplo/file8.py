# -*- coding: utf-8 -*-
#!/usr/bin/env python
from file5 import Animalito
class Cielo(Animalito):
    def __init__(self):
        print "Animales Voladores"
        self.datos()
        self.mostrar()
    def habitat(self):
        print "Este animal se mueve en el cielo."
        print "Tiene pulmones."
    def desplazamiento(self):
        print "Este animal se mueve mediante el vuelo"
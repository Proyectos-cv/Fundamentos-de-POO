
class error(Exception):
   def __init__(self):
       print"el primer numero debe ser mayor"

class negativo(Exception):
    def __init__(self):
        print"solo puedes introducir numeros positivos"
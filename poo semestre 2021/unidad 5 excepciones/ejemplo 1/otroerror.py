# -*- coding: utf-8 -*-
# #!/usr/bin/env python
class OtrosErrores:
    def tratandoErrores(self):
        try:
            n = float(input("Introduce un numero divisor: "))
            x= 5/n
        except NameError as e:
            #print("No se puede dividir el numero entre una cadena",type(e).__name__)
            raise NameError("No se puede dividir el numero entre una cadena")
        except ValueError as e:
            #print("Debes introducir una cadena que sea un numero",type(e).__name__)
            raise ValueError("Debes introducir una cadena que sea un numero")
        except ZeroDivisionError as e:
            #print("No se puede dividir por cero, prueba otro numero", type(e).__name__)
            raise ZeroDivisionError("No se puede dividir por cero, prueba otro numero")
        except Exception as e:
            #print("Ha ocurrido un error no previsto", type(e).__name__ )
            raise Exception("Ha ocurrido un error no previsto")
        finally:
            print "Hemos terminado el programa"

error=OtrosErrores()
error.tratandoErrores()


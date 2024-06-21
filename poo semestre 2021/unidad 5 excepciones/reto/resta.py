from exept import error
from exept import negativo
class rest:
    def operar(self):
        try:
            a=int(input("dame el primer numero: "))
            n = int(input("dame el primer numero: "))
            if a<0 or n<0:
                raise negativo
            elif a<n:
                raise error
            else:
                x=a-n
            print x
        except NameError:
            raise NameError("introduce un numero")
        except error:
            print error
        except negativo:
            print negativo
        except Exception:
            raise Exception("error de simbolo")
j=rest()
j.operar()
class Marinero:
    def saludar(self):
        return "hola..."

class Pulpo(Marinero):
    def saludar(self):
        return "hola soy un pulpo"


class Foca(Marinero):
    def saludar(self,mensaje):
        print(super().saludar())
        print(Marinero.saludar(self))
        return f"hola {mensaje}"


    '''def __init__(self,mensaje):
        self._mensaje=mensaje

    @property
    def mensaje(self):
        return self._mensaje
    
    @mensaje.setter
    def mensaje(self,otro):
        self._mensaje=otro'''

obj=Foca()
msj=obj.saludar("foca")
print(msj)

print(":..............:")
objt=Marinero()
mj=objt.saludar()
print(mj)
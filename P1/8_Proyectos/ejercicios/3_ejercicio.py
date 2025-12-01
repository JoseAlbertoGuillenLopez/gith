class Fabrica:
    def __init__(self,llantas,color,precio):
        self._llantas=llantas
        self._color=color
        self._precio=precio

    def getllantas(self):
        return self._llantas
    
    def setllantas(self,otro):
        self._llantas=otro

    def getcolor(self):
        return self._color
    
    def setcolor(self,otro):
        self._color=otro

    def getprecio(self):
        return self._precio
    
    def setprecio(self,otro):
        self._precio=otro

class Moto(Fabrica):
    def __init__(self,llantas, color, precio, tipomoto):
        super().__init__(llantas, color, precio,)
        self._tipomoto=tipomoto

    def gettipomoto(self):
        return self._tipomoto
    
    def settipomoto(self,otro):
        self._tipomoto=otro

class Carro(Fabrica):
    def __init__(self,llantas, color, precio,tipocarro):
        super().__init__(llantas, color, precio)
        #Fabrica().__init__(llantas, color, precio) super o fabrica de las 2 se puede
        self._tipocarro=tipocarro

    def gettipocarro(self):
        return self._tipocarro
    
    def settipocarro(self,otro):
        self._tipocarro=otro

    '''def acelerar(self):
        super().acelerar()
        #hace que se llamane los metodo o atributos de la padre
        #es como static method pero sin el statiic y pongo super y es sin crear objeto
        print("mas rapido")'''
        

#obj1=Moto(2,"rojo",1200,"sport")

llantas=input("llantas: ")
color=input("color: ")
precio=float(input("precio: "))
tipo1=input("tipo: ")
obj1=Moto(llantas,color,precio,tipo1)

llantas2=input("llantas: ")
color2=input("color: ")
precio2=float(input("precio: "))
tipo2=input("tipo: ")
obj2=Carro(llantas2,color2,precio2,tipo2)

print(f"vehiculo con llantas {obj1.getllantas()} color {obj1.getcolor()} precio {obj1.getprecio()} tipo {obj1.gettipomoto()}")
print(f"vehiculo con llantas {obj2.getllantas()} color {obj2.getcolor()} precio {obj2.getprecio()} tipo {obj2.gettipocarro()}")

#parcial 2 solo proyectos consola en git
#vid
#practicas
#main en class en notas y coches



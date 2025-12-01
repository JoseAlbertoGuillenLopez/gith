class Figuras:
    def __init__(self,x,y,visible):
        self.x=x
        self.y=y
        self.visible=visible

    def estaVisible(self):
        return self.visible
    
    def mostrar(self):
        self.visible=True
        return f"Figura mostrada"
    
    def ocultar(self): 
        self.visible=False
        return f"Figura oculta"

    def mover(self,otro,otro2):  
        self.x=otro
        self.y=otro2

    def calcularArea(self):  
        return None
    
class Rectangulos(Figuras):
    def __init__(self, x, y, visible,alto,ancho):
        super().__init__(x, y, visible)
        self.__alto=alto
        self.__ancho=ancho

    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self,otro):
        self.__alto=otro

    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self,otro):
        self.__ancho=otro

    def ocultar(self):  
        self.visible=False
        return "Rectangulo oculto"

    def mostrar(self):
        self.visible=True
        return "Rectangulo visible"
    
    def calcularArea(self): 
        return float(self.__alto * self.__ancho)
    
class Circulos(Figuras):
    def __init__(self, x, y, visible,radio):
        super().__init__(x, y, visible)
        self.__radio=radio

    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self,otro):
        self.__radio=otro

    def ocultar(self):  
        self.visible=False
        return "Circulo oculto"

    def mostrar(self):
        self.visible=True
        return "Circulo visible"
    
    def calcularArea(self): 
        return float(3.1416*(self.__radio*self.__radio))
    
rectangulo1=Rectangulos(3,4,True,10,20)
circulo1=Circulos(3,3,True,6)

op=rectangulo1()
print(op)
            

'''calcular aree(radio,ancho): float
visible:bool
mover (int,int)'''

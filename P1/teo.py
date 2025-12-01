
#si quiero hablar a un metodo dentro de otro tengo que usar el self.
#todo metodo u atributo dentro de la clase para trabajar con el se usa self.
class person:
    def __init__(self,nom):
        self.nom=nom

    def salu(self):
        print(f"hola soy {self.nom}")

    def cond(self):
        if self.nom=="juan":
            self.salu()
            pass
        else:
            print("tu no eres juan")


p1=person("juan")
p1.cond()



#cuando hay un atributo estatico privado accedo a el con el nombre de las clase.   Carros.__ruedas
#cuando hay un atriibuto de init proivado acedo a el con el self.   self.__ruedas
#si no quiero usar el init lo puedo poner como otro metodo pero luego tengo que mandarlo a llamar y llenar los parametros
#atributos publicos= son interfaces y no cambian    atributos privados son=implementaciones y pueden cambiar pero no importa porque son mas para que los devs lo vean
# name mangling=__ es privado y puede ser para atributos y metodos
#las propiedades o decoradores son como getters y setters pero de otra manera, se definen como una funcion pero si se quiere mostrar o modificar es como si fueran variables
# @property=para getter   @nombre del getter.setter  @nombre del getter.deleter  del objeto.atributo  
#@classmethod metodo de clase con paraemtro cls y se usan con los atributos de clase
#un metodo estatico no tiene parametro inicual como self y se uda con decorador
# metodos dunner o magicos son __  __ son como fnciones ya craedas como sumar restar mult ordenar, longitud tambien sirven oara comparar como operadores reladcionales
#super se usa para acceder a los metodos y atributos de la clase padre si sobreescribes abajo los mismos metodos o atributos
# student(person,worker) multiple herenciaa y se una MRO para la jerarquia de atributos o metodos en las clases hijas

#si quiero usar listas con conjunto de objetos es:

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def mostrar(self):
        print(self.author, self.title)

book1=Book("lotr1","yo")
book2=Book("lotr2","tu")
book3=Book("lotr3","el")

libros=[book1,book2,book3]
#print(libros) no se puede tiene que ser con un for y tengo que imprimir los atributos y puedo usarlo con i.atributo aqui se crea otro objeto
for i in libros:
    print(i.author,i.title)
    if i.author=="tu":
        print("eres tu")
    else:
        pass

#puedo hacer un metodo que muestre y solo lo uso al final con i. AL HACER EL FOR I IN LIBROS AUTOMATICAMENTE I SE COMBVIERE EN EL OBJETO DE SU POICION
for i in libros:
    i.mostrar()

book4=Book("lotr4", "yo")
libros.append(book4)

book0 = Book("lotr0", "yo")
libros.insert(0, book0)

libros.remove(book2)

libros.pop(0)

pos = libros.index(book3)

print(libros.count(book1))

libros.reverse()
for i in libros:
    print(i.author,i.title)












class book:
    x=5
    def __init__(self, x=100):
        self.x=x

b1=book()

print(book.x)
print(b1.x)
print(book.x)
print(b1.x)
#puedo usar la misma variable una de clase y la otra de obj o funcion y darle valor diferente pero seguria siendo estatico en la funcion pero para que 
#se pueda utilizar la misma le agrego el self



#para usar un conatdor
class person:
    conta=0
    def __init__(self,nombre):
        self.nombre=nombre
        person.conta=person.conta+1
    def saludos(Self):
        print(f"hola soy {Self.nombre} y mi numero es {person.conta}")

p1=person("jose")
p1.saludos()
p2=person("juan")
p2.saludos()


#ver listas  property y tkinter


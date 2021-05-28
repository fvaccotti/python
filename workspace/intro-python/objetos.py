#Objetos, clases y herencia

class Usuario:
    def __init__(self, nombre, apellido):
            self.nombre = nombre
            self.apellido = apellido
    #si o si, palabra reservada
    #nombre = "Felipe" #nombre por defecto
    #apellido = "Feliz" #apellido por defecto
    def saludo(self): #referencia a si mismo, no recibe nada. El primer argumento del metodo siempre es el self
        print('Hola!, mi nombre es: ', self.nombre, self.apellido)

##Herencia
class Admin(Usuario): #es la forma de escribir la herencia, entre ()
    def superSaludo(self):
        print('Hola! me llamo, ', self.nombre, ' y soy admin')

#usuario = Usuario('Felipe', 'Feliz')
#usuario.saludo()
#usuario.nombre = 'Chanchito'
#usuario.saludo()

#admin = Admin('Admin', 'Sarasa')
#admin.saludo()
#admin.superSaludo()

#Tambien se pueden eliminar las propiedades

#del usuario.nombre
#usuario.saludo() #va a dar error porque nombre se volo

#eliminar un objeto por completo
#del usuario

class Animal: 
    def __init__(self, nombre, onomatopeya): 
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un: ', self.tipo, 'y mi sonido es el: ', self.onomatopeya)    

#el metodo init se puede querer extender en los hijos
class Gato(Animal):
    tipo = 'gato' 
    def __init__(self, nombre, onomatopeya): #hace un override de la clase padre
        Animal.__init__(self, nombre, onomatopeya) #si quiero que se ejecute el padre
        print('Hola soy un gato extendido')
   
class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya): #usando super
        super().__init__(nombre, onomatopeya) #aca no se necesita self, usando super. 
        print('Instanciando un perro')
        
class Canario(Animal):
    tipo = 'canario'

gato = Gato('Mile', 'maullido')
gato.saludo()
perro = Perro('Bobby', 'ladrido')
perro.saludo()
canario = Canario('Jimmy', 'silvido')
canario.saludo()


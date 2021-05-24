#Comentarios. 
if 3 > 5:
    print('Esto no se va a imprimir')

if 5 > 3: #con un comentario para ver que se ignora
    print('5 Es mayor a 3')

x = 5
y = 'chanchito feliz'

#print(x, y)

email = 'chanchito@feliz.com'

#print(email)

mivar = 'chanchito'
mi_var = 'chanchito'
miVar = 'chanchito'
MIVAR = 'chanchito' #las mayusculas se utilizan siempre para constantes en general

#multiples variables
a, b, c = 'Lala', 'Lele', 'Lili'
#print(a,b,c) #ya pone solos los espacios

valor1 = valor2 = valor3 = 'Chanchito Feliz'
#print(valor1, valor2, valor3)

#concatenacion
inicio = 'Hola ' #sin el espacio, la concatenacion queda pegada
final = 'Mundo'

#print(inicio + final)

#Diferentes tipos de datos
#String
palabra = 'hola'
oracion = "hola mundo con comilla doble"

#Numeros. Enteros(integer), float y complejos
entero = 20
conDecimales = 20.2
complejo = 1j #numero complejo, con la j por convencion. 

#print(palabra, oracion, entero, conDecimales, complejo)

################################################Listas#########################################################################
#lista = [] #lista vacia
lista = ['Hola', 'Mundo', 'Chanchito Feliz']

#generar una copia de la lista al momento de la copia. Si lista original cambia luego de la copia, lista2 no se entera
lista2 = lista.copy()

#agregar elemento a la lista
#lista.append(4)
lista.append('Chanchito triste')
#limpiar la lista (elimina todos los elementos)
#lista.clear()

#print(lista)
#print(lista2)
#contar repeticiones de un valor
#print(lista.count(1))

#longitud de la lista
#print(len(lista), len(lista2))
largoLista = len(lista)
largoLista2 = len(lista2)

#print(largoLista, largoLista2)

#Accediendo a elementos de una lista
#print(lista[0]) #arrancan en 0

#Eliminar elementos de la lista
#print(lista)
#lista.pop() #elimina el ultimo elemento de la lista
#print(lista)

#Eliminar elemento en particular
#lista.remove('Hola') #elimina el elemento puntual
#print(lista)

#Manejo de listas. Reverse y sort
#print(lista)
lista.reverse()
lista.sort() #no se puede ordenar con este metodo cuando se usa strings y numeros mezclados. Para ordernarlas deben ser del mismo tipo de datos
#print(lista)

################################################Tuplas#########################################################################
#Es lo mismo que una lista pero es inmutable, no se puede modificar
#listas --> []
#tuplas --> ()

tupla = ('hola', 'mundo', 'somos', 'tupla')
#print(tupla)

#print(tupla.count('mundo'))
#print(tupla.index('hola'))
#print(tupla[0])

#para poderla modificar hay que transformarla la tupla en una tupla
listaDeTupla = list(tupla)
listaDeTupla.append(10)
#print(listaDeTupla) #ahora si es modificable pero es otra variable y no es mas la tupla

###################################################Range#################################################################
#muchos elementos desde un rango inicial y final. Sirve para las iteraciones

rango = range(6)
#print(rango)

###################################################Diccionarios#################################################################
#como listas pero para acceder a un indice sin usar numeros. Clave-valor

diccionario = {
    "nombre": "Mile",
    "raza": "calico",
    "edad": 1
}

#print(diccionario)
#print(diccionario['nombre'])
#print(diccionario['raza'])
#print(diccionario['edad'])
#print(diccionario.get('nombre'))
#print(diccionario.get('raza'))
#print(diccionario.get('edad'))

#para cambiar un valor del diccionario puedo poner:
diccionario['edad'] = '8 meses'
#print(diccionario)
#print(diccionario.get('nombre'))
#print(diccionario.get('raza'))
#print(diccionario.get('edad'))
#print(len(diccionario))

#agregar una nueva propiedad al diccionario
diccionario['ronronea'] = 'Si'
#print(diccionario)

#eliminar una propiedad
diccionario.pop('ronronea') #uno puntual
diccionario.popitem() #elimina el ultimo agregado
del diccionario['nombre'] #del es la palabra reservada para eliminar
#print(diccionario)

#copiar el diccionario
copiaDiccionario = diccionario.copy()
copiaDiccionarioDos = dict(diccionario) #es otra forma de copiar
#print(copiaDiccionario)
#print(copiaDiccionarioDos)

#eliminar todos los elementos
diccionario.clear()

#diccionarios anidados
gatitos2 = {
    "Fluffy": {
        "nombre": "Fluffy",
        "edad": 4
    },
    "Mamba": {
        "nombre": "Black Mamba",
        "edad": 12
    }
}

#forma 2
fluffy = {
        "nombre": "Fluffy",
        "edad": 4
    }
mamba = {
        "nombre": "Black Mamba",
        "edad": 12
    }
gatitos = {
    "Fluffy": fluffy,
    "Mamba": mamba
}

#print(gatitos2)
#print(gatitos)

#otra forma para crear diccionarios es para usar el constructor dict
perritos = dict(nombre="Bobby", edad=12, raza="nn") #no son necesarias las comillas en las claves, solo en los valores
print(perritos)

#todas las formas de crear los diccionarios es VALIDA, no hay mejores ni peores.

###########################Booleanos##############################
verdadero = True
falso = False
print(verdadero, falso)





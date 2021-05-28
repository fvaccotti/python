#Funciones
#usamos la palabra reservada def para definir funciones

def miFuncion():
    print('Mi primera funcion!')

#miFuncion()

def imprimeDato(argumentoUno): #la funcion recibe argumentos y al llamar pasamos parametros
    print('Mi argumento es: ', argumentoUno)

imprimeDato("Hola Mundo!")
imprimeDato(29)

def imprimeMasArgumentos(nombre, apellido):
    print('El nombre completo es: ', nombre, apellido)

imprimeMasArgumentos('Faby', 'Chubi')

#cantidad variable de argumentos
def funcArgumentosVariables(*nombre): #*nombre, el nombre lo toma como una lista de args
    print('El nombre completo es: ', nombre)
#se puede acceder a los indices nombre[2], iterar con for

funcArgumentosVariables('Holis', 'como','estas?', 20)#lo muestra como tupla. Inmodificable

#Utilizando nombre de argumentos como parametros y no se el orden
def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

nombreCompleto(nombre='Faby', apellido='Sarasa')

#otra forma. Acceder a los argumentos con la sintaxis de diccionarios
def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido']) 

nombreCompleto2(nombre='Faby', apellido='Sarasa')

#tomando un valor por defecto
def miFuncion2(argumento = 'Chanchito'):
    print(argumento)

miFuncion2('Batman')
miFuncion2() #sin parametro, toma el valor defecto

#pasar una lista directo de argumentos
def miFuncionLista(lista):
    for el in lista:
        print(el)

miFuncionLista(['Chanchito', 'Feliz', 23])

#funciones con retorno
def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + ' ' + el
    return i

nombres = concatenaNombres(['Chanchito', 'Feliz'])
print(nombres)

#Recursividad
def recursion(i):
    if(i < 1):
        return i #detiene la ejecucion aca cuando se cumpla
    print(i)
    recursion(i - 1)

recursion(5)
#Reintentos a una api o base de datos con recursividad seria una buena forma
#Procesamiento en batch es otro ejemplo


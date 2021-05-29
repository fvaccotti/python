#multiplicar dos numeros sin usar el simbolo de multiplicacion
print('##Ejercicio 1##')
a = 4
b = 8
resultado = 0 

for x in range(a):
    resultado += b

print('El resultado es: ', resultado)

#ingresar nombre y apellido e imprimirlo al reves
print('\n##Ejercicio 2##')
nombre = 'Faby'
apellido = 'Chubi'

concatenacion = nombre + ' ' + apellido
print('El string invertido es: ', concatenacion[::-1]) #para dar vuelta un string

#escribir una funcion que encuentre el elemento menor de una lista
print('\n##Ejercicio 3##')

lista = [1, 2, 5, 3, 55, -24, -13]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor

print('El valor menor es: ', menor)

#escribir una funcion que devuelva el volumen de una esfera por su radio
#4/3 * pi * r ** 3
print('\n##Ejercicio 4##')

def calculaVolumen(r):
    return 4 / 3 * 3.14 * r ** 3 #en python la doble ** es un exponente

resultado = calculaVolumen(6)
print('El volumen es: ', resultado)

#escribir una funcion que indique si el usuario es mayor de edad
print('\n##Ejercicio 5##')

def esMayor(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario1 = Usuario(15)
usuario2 = Usuario(21)

resultado1 = esMayor(usuario1)
resultado2 = esMayor(usuario2)

print('Mayores o no: ', resultado1,resultado2)

#escribir una funcion que indique si un numero es par o impar
print('\n##Ejercicio 6##')

def esPar(n):
    return n % 2 == 0

resultado = esPar(10)
print('El numero es par: ', resultado)

resultado = esPar(11)
print('El numero es par: ', resultado)

#escribir una funcion que indique cuantas vocales tiene una palabra
print('\n##Ejercicio 7##')

palabra = 'FabianaEsteban'
vocales = 0

for x in palabra:
    y = x.lower() #pasa todo a minuscula para que tambien tome las mayus
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

print('La palabra ', palabra, 'tiene ', vocales, 'vocales')

#escribir una aplicacion que reciba una cantidad infinita de numeros hasta decir basta
#luego que devuelva la suma de los numeros ingresados
print('\n##Ejercicio 8##')

lista = []
print('Ingrese numeros y para salir escriba "basta"')

while True:
    dato = input('Ingrese valor: ')
    if dato == 'basta':
        break
    else:
        try:
            valor = int(dato)
            lista.append(valor)
        except:
            print('El dato no es valido')
            exit()

resultado = 0
for x in lista:
    resultado += x

print('La suma es: ', resultado)


#escribir una funcion que reciba nombre y apellidos y los vaya agregando a un archivo
print('\n##Ejercicio 9##')

def agregaNombres(nombre, apellido):
    c = open('listado.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

agregaNombres('Fabiana', 'Sarasa')
agregaNombres('Chubi', 'Sarasa')

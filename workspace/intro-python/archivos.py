#Manejo de archivos

#c = open('prueba.txt') #sin indicar permisos, si no lo ponemos por defecto es read
c = open('prueba.txt', 'a')
#Permisos
#r - read
#a - append (agregar cosas al file)
#w - write (modificarlo completamente. Si el archivo no existe lo crea, si existe lo abre y pisa todo)
#x - para crearlo. Si existe, devuelve un error


#print(c.read()) #para leer la totalidad del archivo es read

#para leer linea a linea
#print(c.readline())

#for x in c: #leyendo linea a linea. x es una linea
#    print(x)

c.write('\nagregamos una linea al archivo')
c.close()

x = open('prueba.txt')
print(x.read())

#Eliminar archivos - utilizando una libreria / modulo de python
import os

if(os.path.exists('prueba.txt')):
    os.remove('prueba.txt')
else:
    print('el archivo no existe')

#Para eliminar una carpeta
#os.rmdir('micarpeta')


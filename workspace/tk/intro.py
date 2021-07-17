from tkinter import *
#Libreria para bindear Python con opciones graficas
#Permite hacer widgets

root = Tk()
root.title('Hola Mundo')
root.geometry('400x400') #para indicar las dimensiones al abrir - anchoxalto

l1= Label(root, text='Hola mundo! mi primera etiqueta') #args: donde quiero la etiqueta, que texto queres mostrar
l2= Label(root, text='Hola mundo! mi segunda etiqueta') 
#l1.pack() #para que el elemento sea visible

l1.grid(row=0, column=0) #grid permite manejar estructura de grilla y darle un orden a los datos
l2.grid(row=1, column=1)

root.mainloop() #es necesario para actualizar los cambios en la vista

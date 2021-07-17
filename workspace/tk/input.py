from tkinter import *

root = Tk()
root.title('Hola Mundo')
root.geometry('500x500')

e = Entry(root, width=60 ) #Elemento de input. args: donde, ancho
e.pack()
e.insert(0, 'Ingresa texto') #tomar texto de cualquier lado. Args: indice, texto

def click():
    texto = e.get() #toma el valor de la entrada del input
    textvariable.set(texto)
    #l.configure(text=texto) #configure para setearle el valor al label
    e.delete(0, END) #limpia el input
 
btn = Button(root, text='click', command=click)
btn.pack()

textvariable = StringVar() #trabajando con variables y no directamente con la etiqueta
#l = Label(root, text='Texto de la etiqueta')
l = Label(root, textvariable=textvariable)
l.pack()

root.mainloop()
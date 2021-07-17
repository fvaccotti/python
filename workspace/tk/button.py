from tkinter import *

root = Tk()
root.title('Hola Mundo!')
l = Label(root, text='me apretaste')

def click():
    l.pack() #solo para mostrarla 

#args: donde sera mostrado, texto del boton, funcion de reaccion con command (sin los () de ejecucion porque es responsabilidad del boton)
#estilado: fg (foreground) el color del texto, bg background del boton pero en mac no anda. Solo en windows/linux
btn = Button(root, text='Click', command=click, fg='red', bg='black') 
btn.pack()

root.mainloop()
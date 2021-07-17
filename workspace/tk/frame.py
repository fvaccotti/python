from tkinter import *

root = Tk()
root.title('Hola Mundo')

#LabelFrame se utiliza para agrupar contenido que creamos que tiene sentido junto. tiene el texto y el recuadro
#frame = LabelFrame(root, text='Login', padx=10, pady=10, borderwidth=10) #Padding dentro del frame. El nombre puede ir o no (el login). 
frame = Frame(root, padx=10, pady=10)
frame.pack(padx=50, pady=50) #propiedades para pasarle al frame. Padding fuera del frame

l = Label(frame, text='Estoy dentro de un frame')
btn = Button(frame, text='Salir', command=root.quit) #root.quit cierra la aplicacion
l.pack()
btn.pack()

root.mainloop()
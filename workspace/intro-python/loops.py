#While

i = 0

while i < 5:
    i += 1
    if i == 3:
        #break
        continue #va a saltearse lo que sigue (el incremento de i) y vuelve al while
    print(i)
#cuando i == 3 el continue se saltea el print y por eso no muestra el 3

#For
usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']

for usuario in usuarios:
    if usuario == 'roberto':
        #continue #va a ignorar la impresion de roberto
        break #va a cortar cuando llegue roberto y no lo imprime
    print(usuario)

#For usando range
#for x in range(6): #asi arranca en 0. con (2, 6) , 2 sera el valor inicial
for x in range(1, 10, 2): #el 2 final indica que salte de a 2
    print(x)
else: ##se puede agregar la condicion de else como condicion de fin de los for
    print('Hemos terminado!')

#For anidado
edades = [24, 25, 26, 35]

for usuario in usuarios:
    for edad in edades:
        print(usuario, edad)

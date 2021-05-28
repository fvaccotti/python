#Traer info del usuario
#Funcion input
#dato = input('Ingrese dato: ')

#lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']
#if lista.count(dato) > 0:
#    print('El dato existe: ', dato)
#else:
#    print('El dato no existe :(', dato)

#Calculadora
primer = input('Ingrese primer numero: ')

try:
    primero = int(primer)
except:
    primero = 'Chanchito feliz. Fallaste!'

if primero == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

segundo = input('Ingrese el segundo numero: ')

#print(primero + segundo) #concatena porque lo toma como que son strings desde input 
try:
    segund = int(segundo)
except:
    segund = 'Chanchito feliz. Fallaste!'

#si metemos basura, tenemos que ver si podemos transformar el numero a un entero
if segund == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

simbolo = input('Ingrese el simbolo: ')

if simbolo == '+':
    print('Suma: ', primero + segund)
elif simbolo == '-':
    print('Resta: ', primero - segund)
elif simbolo == '*':
    print('Multiplicacion: ', primero * segund)
elif simbolo == '/':
    print('Division: ', primero / segund)
else:
    print('El simbolo no es correcto')




if 2 < 5:
    print('2 es menor que 5')

#a == b
#a < b
#a > b
#a != b
#a <= b
#a >= b

#if con elif y else
if 2 > 5:
    print('lala')
elif 2 == 5:
    print('lele')
else: 
    print('2 es menor a 5')

if 3 == 4:
    print('3 es igual a 4')
else:
    print('3 no es igual a 4')

#otras forma de escribir
if 2 < 5: print('2 es menor a 5 en una linea')

print('cuando vuelve true') if 5 > 2 else print(' cuando devuelve false') #operador ternario

#and y or
if 2 < 5 and 3 < 4:
    print('el and funciona porque ambas devuelven true')

if 2 < 5 and 3 > 4:
    print('el and no se imprime porque una es falsa')

if 1 < 0 or 3 > 2:
    print('como es un or me alcanza con un true')
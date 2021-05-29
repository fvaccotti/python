#import modulos as xs #import <filename>. Escribiendo 'as' podemos renombrar el modulo
#cuando queremos importar algo del modulo, no todo. Por ej solo el saludo. Separando por coma vamos agregando solo lo que nos interesa

from modulos import saludo, mascotas
from camelcase import CamelCase #aunque lo subraya funciona igual

print(mascotas)
saludo('Faby')
#print(xs.mascotas)
#xs.saludo('Faby')

#pip nos permite gestionar los paquetes instalados en python. Nos permite listar los modulos que tenemos, agregar y eliminar
#pypi.org para buscar un paquete en particular y lo podamos usar
#buscamos uno en particular y te dice como instalarlo y como usarlo
#pip list --> muestra la lista de modulos instalados
#pip unistall <nombremodulo>  --> desinstala un modulo en particular
#la mayoria de las funcionalidades ya estan escritas en algun modulo que resuelva nuestro problema, antes de programar buscar en esta pagina.

c = CamelCase()
s = 'esta oracion necesita camelcase!'
camelcased = c.hump(s)
print(camelcased)


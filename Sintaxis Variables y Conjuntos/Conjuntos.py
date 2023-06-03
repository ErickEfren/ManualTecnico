# Pedir al usuario que ingrese una lista de números separados por comas
numeros_input = input('Ingrese una lista de números separados por comas: ')

# Convertir la entrada del usuario en una lista de números
numeros = [int(num.strip()) for num in numeros_input.split(',')]

# Pedir al usuario que ingrese una tupla de nombres separados por comas
nombres_input = input('Ingrese una tupla de nombres separados por comas: ')

# Convertir la entrada del usuario en una tupla de nombres
nombres = tuple(nombre.strip() for nombre in nombres_input.split(','))

# Pedir al usuario que ingrese un diccionario de edades en el formato "nombre:edad" separados por comas
edades_input = input('Ingrese un diccionario de edades en el formato "nombre:edad" separados por comas: ')

# Convertir la entrada del usuario en un diccionario de edades
edades = {}
for item in edades_input.split(','):
    nombre, edad = item.split(':')
    edades[nombre.strip()] = int(edad.strip())

# Crear un conjunto de números pares a partir de la lista de números
pares = set(num for num in numeros if num % 2 == 0)

# Imprimir el primer elemento de la lista de números
print(f'El primer número es: {numeros[0]}')

# Imprimir los últimos dos elementos de la lista de números
print(f'Los dos últimos números son: {numeros[-2:]}')

# Recorrer la tupla de nombres e imprimir cada nombre
print('Los nombres son:')
for nombre in nombres:
    print(nombre)

# Pedir al usuario que ingrese un nombre para buscar su edad en el diccionario
nombre_buscar = input('Ingrese un nombre para buscar su edad: ')

# Imprimir la edad del nombre buscado si existe, de lo contrario indicar que no se encontró
if nombre_buscar in edades:
    print(f'{nombre_buscar} tiene {edades[nombre_buscar]} años')
else:
    print(f'No se encontró a {nombre_buscar} en el diccionario de edades')

# Pedir al usuario que ingrese un nombre y una edad para agregar al diccionario
nombre_agregar = input('Ingrese un nombre para agregar al diccionario de edades: ')
edad_agregar = input('Ingrese la edad de la persona: ')

# Agregar la nueva persona al diccionario de edades
edades[nombre_agregar] = int(edad_agregar)

# Imprimir los números pares del conjunto
print('Números pares:')
for num in pares:
    print(num)

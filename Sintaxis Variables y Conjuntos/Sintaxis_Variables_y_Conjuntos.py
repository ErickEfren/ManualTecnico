# Crear una lista de números enteros
numeros = [5, 2, 8, 1, 3, 7, 4, 9, 6]

# append(): Agrega un elemento al final de la lista
numeros.append(10)
print("append():", numeros)

# extend(): Agrega los elementos de una lista a otra lista
numeros.extend([11, 12, 13])
print("extend():", numeros)

# insert(): Inserta un elemento en una posición específica de la lista
numeros.insert(0, 0)
print("insert():", numeros)

# remove(): Elimina el primer elemento de la lista que coincide con el valor dado
numeros.remove(3)
print("remove():", numeros)

# pop(): Elimina y devuelve el último elemento de la lista o el elemento en el índice dado
numeros.pop()
print("pop():", numeros)

numeros.pop(1)
print("pop(index):", numeros)

# clear(): Elimina todos los elementos de la lista
numeros.clear()
print("clear():", numeros)

# index(): Devuelve el índice del primer elemento que coincide con el valor dado
numeros = [5, 2, 8, 1, 3, 7, 4, 9, 6]
print("index():", numeros.index(3))

# count(): Cuenta el número de elementos en la lista que coinciden con el valor dado
print("count():", numeros.count(5))

# sort(): Ordena los elementos de la lista en orden ascendente
numeros.sort()
print("sort():", numeros)

# reverse(): Invierte el orden de los elementos en la lista
numeros.reverse()
print("reverse():", numeros)

# copy(): Crea una copia de la lista
copia_numeros = numeros.copy()
print("copy():", copia_numeros)

print("------------------------------------------------------------------------------")
# Crear un diccionario de personas con sus respectivas edades
personas = {
    "Juan": 25,
    "Ana": 32,
    "Pedro": 19,
    "Maria": 42,
    "Luisa": 27
}

# clear(): Elimina todos los elementos del diccionario
personas.clear()
print("clear():", personas)

# copy(): Crea una copia del diccionario
personas = {
    "Juan": 25,
    "Ana": 32,
    "Pedro": 19,
    "Maria": 42,
    "Luisa": 27
}

copia_personas = personas.copy()
print("copy():", copia_personas)

# fromkeys(): Crea un nuevo diccionario con claves a partir de una secuencia y valores opcionales
nombres = ["Juan", "Ana", "Pedro", "Maria", "Luisa"]
edades = dict.fromkeys(nombres, 0)
print("fromkeys():", edades)

# get(): Devuelve el valor correspondiente a la clave dada
print("get():", personas.get("Juan"))

# items(): Devuelve una lista de tuplas con cada par clave-valor en el diccionario
print("items():", personas.items())

# keys(): Devuelve una lista con todas las claves en el diccionario
print("keys():", personas.keys())

# values(): Devuelve una lista con todos los valores en el diccionario
print("values():", personas.values())

# pop(): Elimina y devuelve el valor correspondiente a la clave dada
juan_edad = personas.pop("Juan")
print("pop():", juan_edad)

# popitem(): Elimina y devuelve un par clave-valor aleatorio del diccionario
nombre, edad = personas.popitem()
print("popitem():", nombre, edad)

# setdefault(): Devuelve el valor correspondiente a la clave dada, si no existe la clave la crea con el valor opcional
print("setdefault():", personas.setdefault("Juan", 0))
print("setdefault():", personas.setdefault("Pablo", 30))

# update(): Agrega los elementos de un diccionario a otro diccionario existente
otros_nombres = {"Pablo": 30, "Sofia": 28}
personas.update(otros_nombres)
print("update():", personas)

print("------------------------------------------------------------------------------")
# Crear una tupla con algunos elementos
frutas = ("manzana", "banana", "naranja", "pera")

# count(): Devuelve el número de veces que aparece un elemento en la tupla
print("count():", frutas.count("manzana"))

# index(): Devuelve el índice de la primera aparición de un elemento en la tupla
print("index():", frutas.index("naranja"))

# len(): Devuelve la longitud de la tupla (el número de elementos)
print("len():", len(frutas))

# max(): Devuelve el elemento de mayor valor en la tupla
numeros = (1, 5, 3, 7, 2)
print("max():", max(numeros))

# min(): Devuelve el elemento de menor valor en la tupla
print("min():", min(numeros))

# sorted(): Devuelve una lista ordenada con los elementos de la tupla
letras = ("d", "c", "a", "b")
print("sorted():", sorted(letras))

# reversed(): Devuelve una secuencia inversa de la tupla
print("reversed():", tuple(reversed(numeros)))

# slice(): Devuelve una sección de la tupla, especificada por un rango de índices
print("slice():", frutas[1:3])

# concatenación: Se pueden concatenar dos o más tuplas utilizando el operador "+"
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print("concatenación:", tupla3)

# multiplicación: Se puede multiplicar una tupla por un número entero para crear una nueva tupla con elementos repetidos
tupla4 = ("a", "b", "c")
tupla5 = tupla4 * 3
print("multiplicación:", tupla5)

# in: Se puede verificar si un elemento está presente en la tupla utilizando el operador "in"
print("in:", "banana" in frutas)

# not in: Se puede verificar si un elemento no está presente en la tupla utilizando el operador "not in"
print("not in:", "kiwi" not in frutas)

print("------------------------------------------------------------------------------")
# Crear un set con algunos elementos
numeros = {1, 3, 5, 7, 9}

# add(): Agrega un elemento al set
numeros.add(11)
print("add():", numeros)

# update(): Agrega múltiples elementos al set
numeros.update([13, 15, 17])
print("update():", numeros)

# remove(): Remueve un elemento específico del set, si no se encuentra, genera un error
numeros.remove(7)
print("remove():", numeros)

# discard(): Remueve un elemento específico del set, si no se encuentra, no genera error
numeros.discard(9)
print("discard():", numeros)

# pop(): Remueve un elemento aleatorio del set y lo devuelve
elemento = numeros.pop()
print("pop():", elemento)
print(numeros)

# clear(): Remueve todos los elementos del set
numeros.clear()
print("clear():", numeros)

# union(): Crea un nuevo set con todos los elementos de dos sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print("union():", set3)

# intersection(): Crea un nuevo set con los elementos comunes de dos sets
set4 = {1, 2, 3, 4}
set5 = {3, 4, 5, 6}
set6 = set4.intersection(set5)
print("intersection():", set6)

# difference(): Crea un nuevo set con los elementos que están en un set pero no en otro
set7 = {1, 2, 3, 4}
set8 = {3, 4, 5, 6}
set9 = set7.difference(set8)
print("difference():", set9)

# symmetric_difference(): Crea un nuevo set con los elementos que están en un set o en otro, pero no en ambos
set10 = {1, 2, 3, 4}
set11 = {3, 4, 5, 6}
set12 = set10.symmetric_difference(set11)
print("symmetric_difference():", set12)

# issubset(): Devuelve True si todos los elementos de un set están en otro set
set13 = {1, 2, 3}
set14 = {1, 2, 3, 4, 5}
print("issubset():", set13.issubset(set14))

# issuperset(): Devuelve True si un set contiene todos los elementos de otro set
set15 = {1, 2, 3, 4, 5}
set16 = {1, 2, 3}
print("issuperset():", set15.issuperset(set16))

# isdisjoint(): Devuelve True si dos sets no tienen elementos en común
set17 = {1, 2, 3}
set18 = {4, 5, 6}
print("isdisjoint():", set17.isdisjoint(set18))

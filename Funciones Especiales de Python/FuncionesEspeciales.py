# Crear una lista de diccionarios que representan mascotas
mascotas = [
    {'nombre': 'Fido', 'especie': 'perro', 'edad': 5},
    {'nombre': 'Molly', 'especie': 'gato', 'edad': 2},
    {'nombre': 'Rocky', 'especie': 'perro', 'edad': 3},
    {'nombre': 'Socks', 'especie': 'gato', 'edad': 4},
    {'nombre': 'Buddy', 'especie': 'perro', 'edad': 1},
    {'nombre': 'Misty', 'especie': 'gato', 'edad': 6}
]

def clasificar_mascotas(mascotas):
    # Crear un diccionario vacío para cada especie
    especies = {}

    # Recorrer cada mascota en la lista
    for i, mascota in enumerate(mascotas):
        # Obtener la especie de la mascota
        especie = mascota['especie']

        # Comprobar si la especie ya está en el diccionario
        if especie not in especies:
            # Si no está, crear una nueva lista vacía para esa especie
            especies[especie] = []

        # Agregar la mascota a la lista correspondiente
        especies[especie].append(mascota)

    # Ordenar las mascotas por edad dentro de cada especie
    for especie, lista_mascotas in especies.items():
        lista_mascotas.sort(key=lambda mascota: mascota['edad'])

    # Devolver el diccionario de especies y mascotas
    return especies

# Obtener el diccionario de especies y mascotas clasificadas
especies_mascotas = clasificar_mascotas(mascotas)

# Comprobar si todas las mascotas tienen al menos 3 años
todas_mayores_de_3 = all(mascota['edad'] >= 3 for mascota in mascotas)
print(f'Todas las mascotas tienen al menos 3 años: {todas_mayores_de_3}')

# Comprobar si alguna mascota tiene al menos 3 años
algunas_mayores_de_3 = any(mascota['edad'] >= 3 for mascota in mascotas)
print(f'Alguna mascota tiene al menos 3 años: {algunas_mayores_de_3}')

# Recorrer y mostrar las mascotas clasificadas por especie y edad
for especie, lista_mascotas in especies_mascotas.items():
    print(f'{especie.capitalize()}s:')
    for mascota in lista_mascotas:
        print(f'- {mascota["nombre"]}, {mascota["edad"]} años')

from Mascota import *

class AdministradorMascotas:
    def __init__(self):
        self.mascotas = []

    def crear_mascota(self):
        nombre = input("Nombre de la mascota: ")
        edad = int(input("Edad de la mascota: "))
        tipo = input("Tipo de la mascota: ")
        raza = input("Raza de la mascota: ")
        mascota = Mascota(nombre, edad, tipo, raza)
        self.mascotas.append(mascota)
        print(f"{nombre} ha sido creado.")

    def seleccionar_mascota(self):
        print("Seleccione una mascota:")
        for i, mascota in enumerate(self.mascotas):
            print(f"{i + 1}. {mascota.nombre}")
        opcion = int(input("Opción: "))
        return self.mascotas[opcion - 1]

    def alimentar_mascota(self):
        mascota = self.seleccionar_mascota()
        mascota.alimentar()

    def ejercitar_mascota(self):
        mascota = self.seleccionar_mascota()
        mascota.ejercitar()

    def saludar_mascota(self):
        mascota = self.seleccionar_mascota()
        mascota.saludar()

    def obtener_informacion_mascota(self):
        mascota = self.seleccionar_mascota()
        mascota.obtener_informacion()
        
    def agregar_habilidad_mascota(self):
        mascota = self.seleccionar_mascota()
        habilidad = input("Nombre de la habilidad: ")
        nivel = int(input("Nivel de la habilidad: "))
        mascota.agregar_habilidad(habilidad, nivel)
    
    def mejorar_habilidad_mascota(self):
        mascota = self.seleccionar_mascota()
        habilidad = input("Nombre de la habilidad a mejorar: ")
        nivel = int(input("Niveles que mejora: "))
        mascota.mejorar_habilidad(habilidad, nivel)
        
    def enfermar_mascota(self):
        mascota = self.seleccionar_mascota()
        enfermedad = input("Enfermedad de la cual se enfermó: ")
        mascota.enfermar(enfermedad)
        
    def curar_mascota(self):
        mascota = self.seleccionar_mascota()
        enfermedad = input("Enfermedad de la cual se curó: ")
        mascota.curar(enfermedad)

administrador_mascotas = AdministradorMascotas()

while True:
    print("""
    1. Crear mascota
    2. Alimentar mascota
    3. Ejercitar mascota
    4. Saludar mascota
    5. Obtener información
    6. Agregar Habilidad
    7. Mejorar Habilidad
    8. Enfermar
    9. Curar
    """)
    opcion = int(input())
    if(opcion == 1):
        administrador_mascotas.crear_mascota()
    elif(opcion == 2):
        administrador_mascotas.alimentar_mascota()
    elif(opcion == 3):
        administrador_mascotas.ejercitar_mascota()
    elif(opcion == 4):
        administrador_mascotas.saludar_mascota()
    elif(opcion == 5):
        administrador_mascotas.obtener_informacion_mascota()
    elif(opcion == 6):
        administrador_mascotas.agregar_habilidad_mascota()
    elif(opcion == 7):
        administrador_mascotas.mejorar_habilidad_mascota()    
    elif(opcion == 8):
        administrador_mascotas.enfermar_mascota()
    elif(opcion == 9):
        administrador_mascotas.curar_mascota()
    else:False
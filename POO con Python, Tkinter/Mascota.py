class Habilidades:
    def __init__(self):
        self.habilidades = {}

    def agregar_habilidad(self, habilidad, nivel):
        self.habilidades[habilidad] = nivel
        print(f"{habilidad} ha sido aprendido por {self.nombre}.")

    def mejorar_habilidad(self, habilidad, nivel):
        if habilidad in self.habilidades:
            self.habilidades[habilidad] += nivel
            print(f"{habilidad} ha sido mejorado a nivel {self.habilidades[habilidad]}.")
        else:
            print(f"{self.nombre} no conoce {habilidad}.")

class Enfermedades:
    def __init__(self):
        self.enfermedades = []

    def enfermar(self, enfermedad):
        self.enfermedades.append(enfermedad)
        print(f"{self.nombre} está enfermo con {enfermedad}.")

    def curar(self, enfermedad):
        if enfermedad in self.enfermedades:
            self.enfermedades.remove(enfermedad)
            print(f"{self.nombre} ha sido curado de {enfermedad}.")
        else:
            print(f"{self.nombre} no está enfermo con {enfermedad}.")

class Mascota(Habilidades, Enfermedades):
    def __init__(self, nombre, edad, tipo, raza):
        Habilidades.__init__(self)
        Enfermedades.__init__(self)
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        self.raza = raza
        self.hambre = 0
        self.salud = 100

    def alimentar(self):
        self.hambre -= 10
        self.salud += 5
        print(f"{self.nombre} ha sido alimentado.")

    def ejercitar(self):
        self.hambre += 10
        self.salud += 10
        print(f"{self.nombre} ha hecho ejercicio.")

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}. Soy un {self.tipo} de raza {self.raza}.")

    def obtener_informacion(self):
        print(f"{self.nombre} es un {self.raza} {self.tipo} de {self.edad} años. Su nivel de hambre es {self.hambre} y su salud es {self.salud}.")
        print(f"Las habilidades de {self.nombre} son: {self.habilidades}")
        print(f"Las enfermedades de {self.nombre} son: {self.enfermedades}")
    
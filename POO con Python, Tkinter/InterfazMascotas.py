import tkinter as tk
from tkinter import ttk
from Mascota import Mascota
mascotas = []
class GUIAdministradorMascotas:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.tipo = "Perro"
        self.raza = ""
        self.index = 0
        self.seleccion = ""
        
        # Crear ventana principal
        self.root = tk.Tk()
        self.root.title("Administrador de Mascotas")
        
        # Crear botones
        self.btn_crear_mascota = tk.Button(self.root, text="Crear mascota", command=self.crear_mascota).pack()
        self.btn_alimentar_mascota = tk.Button(self.root, text="Alimentar mascota", command=lambda:self.seleccionar_mascota(self.btn_alimentar_mascota))
        self.btn_alimentar_mascota.pack()
        self.btn_ejercitar_mascota = tk.Button(self.root, text="Ejercitar mascota", command=lambda:self.seleccionar_mascota(self.btn_ejercitar_mascota))
        self.btn_ejercitar_mascota.pack()
        self.btn_saludar_mascota = tk.Button(self.root, text="Saludar mascota", command=lambda:self.seleccionar_mascota(self.btn_saludar_mascota))
        self.btn_saludar_mascota.pack()
        self.btn_obtener_informacion_mascota = tk.Button(self.root, text="Obtener información de la mascota", command=lambda:self.seleccionar_mascota(self.btn_obtener_informacion_mascota))
        self.btn_obtener_informacion_mascota.pack()
        self.btn_agregar_habilidad_mascota = tk.Button(self.root, text="Agregar habilidad a la mascota", command=lambda:self.seleccionar_mascota(self.btn_agregar_habilidad_mascota))
        self.btn_agregar_habilidad_mascota.pack()
        self.btn_mejorar_habilidad_mascota = tk.Button(self.root, text="Mejorar habilidad de la mascota", command=lambda:self.seleccionar_mascota(self.btn_mejorar_habilidad_mascota))
        self.btn_mejorar_habilidad_mascota.pack()
        self.btn_enfermar_mascota = tk.Button(self.root, text="Enfermar a la mascota", command=lambda:self.seleccionar_mascota(self.btn_enfermar_mascota))
        self.btn_enfermar_mascota.pack()
        self.btn_curar_mascota = tk.Button(self.root, text="Curar a la mascota", command=lambda:self.seleccionar_mascota(self.btn_curar_mascota))
        self.btn_curar_mascota.pack()
        self.btn_salir = tk.Button(self.root, text="Salir", command=self.salir).pack()
        # Iniciar loop principal
        self.root.mainloop()

    def crear_mascota(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Crear mascota")
        
        vcmd = self.root.register(validate_number)
        
        #Crear campos
        self.lbl_nombre_mascota = tk.Label(self.root, text="Nombre de la mascota").pack()
        self.ent_nombre_mascota = tk.Entry(self.root)
        self.ent_nombre_mascota.pack()
        self.lbl_edad_mascota = tk.Label(self.root, text="Edad de la mascota").pack()
        self.ent_edad_mascota = tk.Entry(self.root, validate="key", validatecommand=(vcmd, '%P'))
        self.ent_edad_mascota.pack()
        self.lbl_tipo_mascota = tk.Label(self.root, text="Tipo de la Mascota").pack()
        self.cb_tipo_mascota = ttk.Combobox(self.root, values=["Perro", "Gato","Conejo", "Hurón", "MiniPig"], state="readonly")
        self.cb_tipo_mascota.current(0)
        self.cb_tipo_mascota.pack()
        self.lbl_raza_mascota = tk.Label(self.root, text="Raza de la Mascota").pack()
        self.ent_raza_mascota = tk.Entry(self.root)
        self.ent_raza_mascota.pack()
        self.btn_entrar = tk.Button(self.root, text="Entrar", command=self.guardar).pack()
        self.btn_restart = tk.Button(self.root, text="Volver", command=self.restart).pack()
        
    def guardar(self):
        self.nombre = self.ent_nombre_mascota.get()
        edadT = self.ent_edad_mascota.get()
        self.edad = int(edadT)
        self.tipo= self.cb_tipo_mascota.get()
        self.raza = self.ent_raza_mascota.get()
        mascota = Mascota(self.nombre, self.edad, self.tipo, self.raza)
        mascotas.append(mascota)
        self.root.destroy()
        self.__init__()
        
    def seleccionar_mascota(self, boton):
        self.seleccion = boton.cget('text')
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Seleccionar mascota")
        seleccion = []
        
        for i, mascota in enumerate(mascotas):
            seleccion.append(mascota.nombre)
            seleccion = sorted(seleccion)
        self.lbl_seleccionar_mascota = tk.Label(self.root, text="Elige la mascota").pack()
        self.cb_index_mascota = ttk.Combobox(self.root, values=seleccion, state="readonly")
        self.cb_index_mascota.current(0)
        self.cb_index_mascota.pack()
        self.btn_seguir = tk.Button(self.root, text="Seleccionar", command=self.seleccionar).pack()
        self.btn_restart = tk.Button(self.root, text="Volver", command=self.restart).pack()
        
    def seleccionar(self):
        indexT = self.cb_index_mascota.get()
        for i,mascota in enumerate(mascotas):
            if mascota.nombre == indexT:
                self.index = i
            else:pass
        if self.seleccion == "Alimentar mascota":
            self.alimentar_mascota()
        elif self.seleccion == "Ejercitar mascota":
            self.ejercitar_mascota()
        elif self.seleccion == "Saludar mascota":
            self.saludar_mascota()
        elif self.seleccion == "Obtener información de la mascota":
            self.obtener_informacion_mascota()
        elif self.seleccion == "Agregar habilidad a la mascota":
            self.agregar_habilidad_mascota()
        elif self.seleccion == "Mejorar habilidad de la mascota":
            self.mejorar_habilidad_mascota()
        elif self.seleccion == "Enfermar a la mascota":
            self.enfermar_mascota()
        elif self.seleccion == "Curar a la mascota":
            self.curar_mascota()
        
        
    def alimentar_mascota(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Alimentar mascota")
        nombre_mascota = ""
        for i, mascota in enumerate(mascotas):
            if i == self.index:
                nombre_mascota = mascota.nombre
        
        self.lbl_alimentacion_mascota = tk.Label(self.root, text=f"{nombre_mascota} ha sido alimentada").pack()
        self.btn_restart = tk.Button(self.root, text="Volver", command=self.restart).pack()
        mascota = mascotas[self.index]
        mascota.alimentar()

    def ejercitar_mascota(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Ejercitar mascota")
        nombre_mascota = ""
        for i, mascota in enumerate(mascotas):
            if i == self.index:
                nombre_mascota = mascota.nombre
        
        self.lbl_ejercicio_mascota = tk.Label(self.root, text=f"{nombre_mascota} ha sido ejercitado").pack()
        self.btn_restart = tk.Button(self.root, text="Volver", command=self.restart).pack()
        mascota = mascotas[self.index]
        mascota.ejercitar()
        
    def saludar_mascota(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Saludar mascota")
        nombre_mascota = ""
        edad_mascota = 0
        tipo_mascota = ""
        raza_mascota = ""
        for i, mascota in enumerate(mascotas):
            if i == self.index:
                nombre_mascota = mascota.nombre
                edad_mascota = mascota.edad
                tipo_mascota = mascota.tipo
                raza_mascota = mascota.raza
        
        self.lbl_saludo_mascota = tk.Label(self.root, text=f"Hola, soy {nombre_mascota} soy un {tipo_mascota}, de {edad_mascota} año(s), de raza {raza_mascota}").pack()
        self.btn_restart = tk.Button(self.root, text="Volver", command=self.restart).pack()
        mascota = mascotas[self.index]
        mascota.saludar()
        
    def obtener_informacion_mascota(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Obtener información de la mascota")
        nombre_mascota = ""
        edad_mascota = 0
        tipo_mascota = ""
        raza_mascota = ""
        hambre_mascota = 0
        salud_mascota = 0
        habilidades_mascota = {}
        enfermedades_mascota = []
        
        for i, mascota in enumerate(mascotas):
            if i == self.index:
                nombre_mascota = mascota.nombre
                edad_mascota = mascota.edad
                tipo_mascota = mascota.tipo
                raza_mascota = mascota.raza
                hambre_mascota = mascota.hambre
                salud_mascota = mascota.salud
                habilidades_mascota = mascota.habilidades
                enfermedades_mascota = mascota.enfermedades
        self.lbl_nombre_mascota = tk.Label(self.root, text=f"Nombre: {nombre_mascota}").pack()
        self.lbl_edad_mascota = tk.Label(self.root, text=f"Edad: {edad_mascota}").pack()
        self.lbl_tipo_mascota = tk.Label(self.root, text=f"Tipo: {tipo_mascota}").pack()
        self.lbl_raza_mascota = tk.Label(self.root, text=f"Raza: {raza_mascota}").pack()
        self.lbl_hambre_mascota = tk.Label(self.root, text=f"Hambre: {hambre_mascota}").pack()
        self.lbl_salud_mascota = tk.Label(self.root, text=f"Salud: {salud_mascota}").pack()
        self.lbl_habilidades_mascota = tk.Label(self.root, text=f"Habilidades: {habilidades_mascota}").pack()
        self.lbl_enfermedades_mascota = tk.Label(self.root, text=f"Enfermedades: {enfermedades_mascota}").pack()                         
        self.btn_restart = tk.Button(self.root, text="Volver", command=self.restart).pack()
        mascota = mascotas[self.index]
        mascota.obtener_informacion()
    
    def agregar_habilidad_mascota(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Agregar habilidad de la mascota")
        
        vcmd = self.root.register(validate_number)
        
        self.lbl_habilidad_mascota = tk.Label(self.root, text="Nombre de la habilidad").pack()
        self.ent_habilidad_mascota = tk.Entry(self.root)
        self.ent_habilidad_mascota.pack()
        self.lbl_nivel_habilidad = tk.Label(self.root, text="Nivel de la habilidad").pack()
        self.ent_nivel_habilidad = tk.Entry(self.root, validate="key", validatecommand=(vcmd, '%P'))
        self.ent_nivel_habilidad.pack()
        self.btn_agregar = tk.Button(self.root, text="Agregar", command=self.agregar).pack()
        self.btn_restart = tk.Button(self.root, text="Volver", command=self.restart).pack()
    
    def agregar(self):
        habilidad = self.ent_habilidad_mascota.get()
        nivel_habilidadT = self.ent_nivel_habilidad.get()
        nivel = int(nivel_habilidadT)
        mascota = mascotas[self.index]
        mascota.agregar_habilidad(habilidad, nivel)
        self.root.destroy()
        self.__init__()
        
    def mejorar_habilidad_mascota(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Mejorar habilidad de la mascota")
        
        vcmd = self.root.register(validate_number)
        
        for i, mascota in enumerate(mascotas):
            if i == self.index:
                habilidades_mascota = mascota.habilidades
        self.lbl_nivel_mejora = tk.Label(self.root, text="Introduce la cantidad de niveles de mejora").pack()
        self.ent_nivel_mejora = tk.Entry(self.root, validate="key", validatecommand=(vcmd, '%P'))
        self.ent_nivel_mejora.pack()
        self.lbl_habilidad_mascota = tk.Label(self.root, text="Selecciona la habilidad").pack()
        self.cb_habilidad_mascota = ttk.Combobox(self.root, values=list(habilidades_mascota.keys()), state="readonly")
        self.cb_habilidad_mascota.current(0)
        self.cb_habilidad_mascota.pack()
        self.btn_mejorar = tk.Button(self.root, text="Mejorar", command=self.mejorar).pack()
        self.btn_restart = tk.Button(self.root, text="Volver", command=self.restart).pack()
        
    def mejorar(self):
        habilidad = self.cb_habilidad_mascota.get()
        nivelT = self.ent_nivel_mejora.get()
        nivel = int(nivelT)
        mascota = mascotas[self.index]
        mascota.mejorar_habilidad(habilidad, nivel)
        self.root.destroy()
        self.__init__()
        
    def enfermar_mascota(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Enfermar mascota")
        
        self.lbl_enfermedad_mascota = tk.Label(self.root, text="Introduce la enfermedad de la mascota").pack()
        self.ent_enfermedad_mascota = tk.Entry(self.root)
        self.ent_enfermedad_mascota.pack()
        self.btn_enfermar = tk.Button(self.root, text="Registar", command=self.enfermar).pack()
        self.btn_restart = tk.Button(self.root, text="Volver", command=self.restart).pack()
    
    def enfermar(self):
        enfermedad = self.ent_enfermedad_mascota.get()
        mascota = mascotas[self.index]
        mascota.enfermar(enfermedad)
        self.root.destroy()
        self.__init__()
    
    def curar_mascota(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Curar mascota")
        
        for i, mascota in enumerate(mascotas):
            if i == self.index:
                enfermedades_mascota = mascota.enfermedades
        
        self.lbl_enfermedad_mascota = tk.Label(self.root, text="Introduce la enfermedad a curar").pack()
        self.cb_enfermedades_mascota = ttk.Combobox(self.root, values=enfermedades_mascota, state="readonly")
        self.cb_enfermedades_mascota.current(0)
        self.cb_enfermedades_mascota.pack()
        self.btn_curar = tk.Button(self.root, text="Curar", command=self.curar).pack()
        self.btn_restart = tk.Button(self.root, text="Volver", command=self.restart).pack()
    
    def curar(self):
        enfermedad = self.cb_enfermedades_mascota.get()
        mascota = mascotas[self.index]
        mascota.curar(enfermedad)
        self.root.destroy()
        self.__init__()
    
    def salir(self):
        self.root.destroy()
        
    def restart(self):
        self.root.destroy()
        self.__init__()

def validate_number(new_value):
    if new_value.isdigit() or new_value == "":
        return True
    else:
        return False
    
Interfaz = GUIAdministradorMascotas()
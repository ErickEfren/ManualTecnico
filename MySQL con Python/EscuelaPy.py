import mysql.connector
from tkinter import *

# Conectarse a la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="n0m3l0",
  database="Escuela"
)

# Crear la ventana principal
root = Tk()
root.title("Aplicación de Escuela")

# Función para mostrar los estudiantes en la tabla
def mostrar_estudiantes():
  # Limpiar la tabla
  for row in estudiantes_table.get_children():
    estudiantes_table.delete(row)
  
  # Obtener los estudiantes de la base de datos
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM Estudiantes")
  estudiantes = mycursor.fetchall()
  
  # Mostrar los estudiantes en la tabla
  for estudiante in estudiantes:
    estudiantes_table.insert("", END, text=estudiante[0], values=(estudiante[1], estudiante[2], estudiante[3], estudiante[4], estudiante[5], estudiante[6]))

# Función para mostrar los cursos en la tabla
def mostrar_cursos():
  # Limpiar la tabla
  for row in cursos_table.get_children():
    cursos_table.delete(row)
  
  # Obtener los cursos de la base de datos
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM Cursos")
  cursos = mycursor.fetchall()
  
  # Mostrar los cursos en la tabla
  for curso in cursos:
    cursos_table.insert("", END, text=curso[0], values=(curso[1], curso[2], curso[3]))

# Función para mostrar los profesores en la tabla
def mostrar_profesores():
  # Limpiar la tabla
  for row in profesores_table.get_children():
    profesores_table.delete(row)
  
  # Obtener los profesores de la base de datos
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM Profesores")
  profesores = mycursor.fetchall()
  
  # Mostrar los profesores en la tabla
  for profesor in profesores:
    profesores_table.insert("", END, text=profesor[0], values=(profesor[1], profesor[2], profesor[3], profesor[4], profesor[5], profesor[6], profesor[7]))

# Función para mostrar las matrículas en la tabla
def mostrar_matriculas():
  # Limpiar la tabla
  for row in matriculas_table.get_children():
    matriculas_table.delete(row)
  
  # Obtener las matrículas de la base de datos
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM Matriculas")
  matriculas = mycursor.fetchall()
  
  # Mostrar las matrículas en la tabla
  for matricula in matriculas:
    matriculas_table.insert("", END, text=matricula[0], values=(matricula[1], matricula[2], matricula[3]))

# Función para mostrar las asignaciones de profesores en la tabla
def mostrar_asignaciones():
  # Limpiar la tabla
  for row in asignaciones_table.get_children():
    asignaciones_table.delete(row)
  
  # Obtener las asignaciones de la base de datos
  mycursor = mydb.cursor()
  mycursor.execute("SELECT Asignaciones.id, Profesores.nombre, Cursos.nombre FROM Asignaciones INNER JOIN Profesores ON Asignaciones.profesor_id = Profesores.id INNER JOIN Cursos ON Asignaciones.curso_id = Cursos.id")
  asignaciones = mycursor.fetchall()
  
  # Mostrar las asignaciones en la tabla
  for asignacion in asignaciones:
    asignaciones_table.insert("", END, text=asignacion[0], values=(asignacion[1], asignacion[2]))

# Crear el marco de los estudiantes
estudiantes_frame = Frame(root)
estudiantes_frame.pack(side=TOP, padx=10, pady=10)

# Crear la etiqueta y la tabla de los estudiantes
estudiantes_label = Label(estudiantes_frame, text="Estudiantes")
estudiantes_label.pack(pady=5)
estudiantes_table = ttk.Treeview(estudiantes_frame, columns=("Nombre", "Apellido", "Edad", "Grado", "Promedio", "Fecha de nacimiento"))
estudiantes_table.heading("#0", text="ID")
estudiantes_table.column("#0", width=50)
estudiantes_table.heading("Nombre", text="Nombre")
estudiantes_table.column("Nombre", width=100)
estudiantes_table.heading("Apellido", text="Apellido")
estudiantes_table.column("Apellido", width=100)
estudiantes_table.heading("Edad", text="Edad")
estudiantes_table.column("Edad", width=50)
estudiantes_table.heading("Grado", text="Grado")
estudiantes_table.column("Grado", width=50)
estudiantes_table.heading("Promedio", text="Promedio")
estudiantes_table.column("Promedio", width=50)
estudiantes_table.heading("Fecha de nacimiento", text="Fecha de nacimiento")
estudiantes_table.column("Fecha de nacimiento", width=150)
estudiantes_table.pack()

# Botón para mostrar los estudiantes en la tabla
estudiantes_button = Button(root, text="Mostrar Estudiantes", command=mostrar_estudiantes)
estudiantes_button.pack(pady=5)

# Crear el marco de los cursos
cursos_frame = Frame(root)
cursos_frame.pack(side=TOP, padx=10, pady=10)

# Crear la etiqueta y la tabla de los cursos
cursos_label = Label(cursos_frame, text="Cursos")
cursos_label.pack(pady=5)
cursos_table = ttk.Treeview(cursos_frame, columns=("Nombre", "Créditos", "Horas"))
cursos_table.heading("#0", text="ID")
cursos_table.column("#0", width=50)
cursos_table.heading("Nombre", text="Nombre")
cursos_table.column("Nombre", width=200)
cursos_table.heading("Créditos", text="Créditos")
cursos_table.column("Créditos", width=50)
cursos_table.heading("Horas", text="Horas")
cursos_table.column("Horas", width=50)
cursos_table.pack()

# Botón para mostrar los cursos en la tabla
cursos_button = Button(root, text="Mostrar Cursos", command=mostrar_cursos)
cursos_button.pack(pady=5)

# Crear el marco de los profesores
profesores_frame = Frame(root)
profesores_frame.pack(side=TOP, padx=10, pady=10)

# Crear la etiqueta y la tabla de los profesores
profesores_label = Label(profesores_frame, text="Profesores")
profesores_label.pack(pady=5)
profesores_table = ttk.Treeview(profesores_frame, columns=("Nombre", "Apellido", "Especialidad"))
profesores_table.heading("#0", text="ID")
profesores_table.column("#0", width=50)
profesores_table.heading("Nombre", text="Nombre")
profesores_table.column("Nombre", width=100)
profesores_table.heading("Apellido", text="Apellido")
profesores_table.column("Apellido", width=100)
profesores_table.heading("Especialidad", text="Especialidad")
profesores_table.column("Especialidad", width=150)
profesores_table.pack()

# Botón para mostrar los profesores en la tabla
profesores_button = Button(root, text="Mostrar Profesores", command=mostrar_profesores)
profesores_button.pack(pady=5)

# Crear el marco de las asignaciones
asignaciones_frame = Frame(root)
asignaciones_frame.pack(side=TOP, padx=10, pady=10)

# Crear la etiqueta y la tabla de las asignaciones
asignaciones_label = Label(asignaciones_frame, text="Asignaciones de Profesores")
asignaciones_label.pack(pady=5)
asignaciones_table = ttk.Treeview(asignaciones_frame, columns=("Profesor", "Curso"))
asignaciones_table.heading("#0", text="ID")
asignaciones_table.column("#0", width=50)
asignaciones_table.heading("Profesor", text="Profesor")
asignaciones_table.column("Profesor", width=150)
asignaciones_table.heading("Curso", text="Curso")
asignaciones_table.column("Curso", width=150)
asignaciones_table.pack()

# Botón para mostrar las asignaciones en la tabla
asignaciones_button = Button(root, text="Mostrar Asignaciones", command=mostrar_asignaciones)
asignaciones_button.pack(pady=5)

# Mostrar la ventana principal
root.mainloop()


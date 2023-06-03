-- Crear la base de datos
CREATE DATABASE Escuela;

-- Usar la base de datos
USE Escuela;

-- Crear la tabla de estudiantes
CREATE TABLE Estudiantes (
  ID_Estudiante INT PRIMARY KEY,
  Nombre VARCHAR(50),
  Apellido VARCHAR(50),
  Fecha_Nacimiento DATE,
  Direccion VARCHAR(100),
  Telefono VARCHAR(20),
  Correo_Electronico VARCHAR(100)
);

-- Crear la tabla de cursos
CREATE TABLE Cursos (
  ID_Curso INT PRIMARY KEY,
  Nombre VARCHAR(50),
  Descripcion VARCHAR(100),
  Creditos INT
);

-- Crear la tabla de profesores
CREATE TABLE Profesores (
  ID_Profesor INT PRIMARY KEY,
  Nombre VARCHAR(50),
  Apellido VARCHAR(50),
  Fecha_Nacimiento DATE,
  Direccion VARCHAR(100),
  Telefono VARCHAR(20),
  Correo_Electronico VARCHAR(100),
  Especialidad VARCHAR(50)
);

-- Crear la tabla de matriculas
CREATE TABLE Matriculas (
  ID_Matricula INT PRIMARY KEY,
  ID_Estudiante INT,
  ID_Curso INT,
  Fecha_Matricula DATE,
  FOREIGN KEY (ID_Estudiante) REFERENCES Estudiantes(ID_Estudiante),
  FOREIGN KEY (ID_Curso) REFERENCES Cursos(ID_Curso)
);

-- Crear la tabla de asignaciones de profesores
CREATE TABLE Asignaciones (
  ID_Asignacion INT PRIMARY KEY,
  ID_Curso INT,
  ID_Profesor INT,
  Ano_Academico INT,
  Semestre INT,
  FOREIGN KEY (ID_Curso) REFERENCES Cursos(ID_Curso),
  FOREIGN KEY (ID_Profesor) REFERENCES Profesores(ID_Profesor)
);

-- Crear la tabla de calificaciones
CREATE TABLE Calificaciones (
  ID_Calificacion INT PRIMARY KEY,
  ID_Matricula INT,
  ID_Asignacion INT,
  Calificacion FLOAT,
  FOREIGN KEY (ID_Matricula) REFERENCES Matriculas(ID_Matricula),
  FOREIGN KEY (ID_Asignacion) REFERENCES Asignaciones(ID_Asignacion)
);

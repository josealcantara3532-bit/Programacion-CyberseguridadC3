CREATE DATABASE ColegioBD;
USE ColegioBD;

CREATE TABLE Departamento (
    DepartamentoID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL
);

CREATE TABLE Estudiante (
    EstudianteID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(150) NOT NULL,
    DepartamentoID INT,
    FOREIGN KEY (DepartamentoID) REFERENCES Departamento(DepartamentoID)
);

CREATE TABLE Profesor (
    ProfesorID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(150) NOT NULL,
    DepartamentoID INT,
    FOREIGN KEY (DepartamentoID) REFERENCES Departamento(DepartamentoID)
);

CREATE TABLE Curso (
    CursoID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(150) NOT NULL,
    Creditos INT NOT NULL
);

CREATE TABLE Clase (
    ClaseID INT PRIMARY KEY AUTO_INCREMENT,
    CursoID INT NOT NULL,
    ProfesorID INT NOT NULL,
    Periodo VARCHAR(20),
    FOREIGN KEY (CursoID) REFERENCES Curso(CursoID),
    FOREIGN KEY (ProfesorID) REFERENCES Profesor(ProfesorID)
);

CREATE TABLE Inscripcion (
    InscripcionID INT PRIMARY KEY AUTO_INCREMENT,
    EstudianteID INT NOT NULL,
    ClaseID INT NOT NULL,
    Fecha DATE,
    FOREIGN KEY (EstudianteID) REFERENCES Estudiante(EstudianteID),
    FOREIGN KEY (ClaseID) REFERENCES Clase(ClaseID)
);

CREATE TABLE Calificacion (
    CalificacionID INT PRIMARY KEY AUTO_INCREMENT,
    InscripcionID INT NOT NULL,
    Nota DECIMAL(5,2) CHECK (Nota BETWEEN 0 AND 100),
    FechaRegistro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (InscripcionID) REFERENCES Inscripcion(InscripcionID)
);

INSERT INTO Departamento (Nombre) VALUES
('Matemáticas'),
('Lengua Española'),
('Historia'),
('Química'),
('Física'),
('Deporte'),
('Arte');


INSERT INTO Profesor (Nombre, DepartamentoID) VALUES
('Prof. Marcos Peña', 1),
('Prof. Laura Medina', 2),
('Prof. Samuel Santos', 3),
('Prof. Daniela Gil', 4),
('Prof. Héctor Ramos', 5),
('Prof. Julia Herrera', 6),
('Prof. Carlos Báez', 7);

INSERT INTO Estudiante (Nombre, DepartamentoID) VALUES
('Ana Martínez', 1),
('Luis Fernández', 1),
('Carlos López', 1),
('María Torres', 2),
('José Ramírez', 2),
('Patricia Díaz', 2),
('Sandra Cruz', 3),
('Pedro Jiménez', 3),
('Lucía Herrera', 3),
('Miguel Castillo', 4),
('Carmen Bautista', 4),
('Eduardo Gómez', 4),
('Sofía Méndez', 5),
('Javier Soto', 5),
('Ricardo Peña', 5),
('Fernando Ruiz', 6),
('Elena Cabrera', 6),
('Daniel Vargas', 7),
('Rosa Almonte', 7),
('Karla Sánchez', 7);

INSERT INTO Curso (Nombre, Creditos) VALUES
('Cálculo I', 4),
('Gramática Española', 3),
('Historia Universal', 3),
('Química General', 4),
('Física I', 4),
('Educación Física', 2),
('Arte y Creatividad', 3);

INSERT INTO Clase (CursoID, ProfesorID, Periodo) VALUES
(1, 1, '2025-1'),
(2, 2, '2025-1'),
(3, 3, '2025-1'),
(4, 4, '2025-1'),
(5, 5, '2025-1'),
(6, 6, '2025-1'),
(7, 7, '2025-1');

INSERT INTO Inscripcion (EstudianteID, ClaseID, Fecha) VALUES
(1, 1, '2025-02-01'),
(2, 1, '2025-02-01'),
(3, 1, '2025-02-01'),
(4, 2, '2025-02-01'),
(5, 2, '2025-02-01'),
(6, 2, '2025-02-01'),
(7, 3, '2025-02-01'),
(8, 3, '2025-02-01'),
(9, 3, '2025-02-01'),
(10, 4, '2025-02-01'),
(11, 4, '2025-02-01'),
(12, 4, '2025-02-01'),
(13, 5, '2025-02-01'),
(14, 5, '2025-02-01'),
(15, 5, '2025-02-01'),
(16, 6, '2025-02-01'),
(17, 6, '2025-02-01'),
(18, 7, '2025-02-01'),
(19, 7, '2025-02-01'),
(20, 7, '2025-02-01');

INSERT INTO Calificacion (InscripcionID, Nota) VALUES
(1, 85.5),
(2, 78.0),
(3, 92.0),
(4, 88.0),
(5, 90.5),
(6, 75.0),
(7, 81.0),
(8, 89.5),
(9, 93.0),
(10, 77.0),
(11, 85.0),
(12, 91.0),
(13, 86.0),
(14, 79.0),
(15, 88.5),
(16, 95.0),
(17, 82.0),
(18, 87.0),
(19, 90.0),
(20, 84.5);

SELECT * FROM Estudiante;
SELECT * FROM Profesor;
SELECT * FROM Curso;
SELECT * FROM Clase;
SELECT * FROM Inscripcion;
SELECT * FROM Calificacion;
SELECT * FROM Estudiante;

SELECT * FROM Estudiante
ORDER BY Nombre ASC;
SELECT * FROM Estudiante
WHERE DepartamentoID = 1;
SELECT * FROM Curso
WHERE Creditos > 3;

SELECT 
    e.Nombre AS Estudiante,
    d.Nombre AS Departamento
FROM Estudiante e
JOIN Departamento d ON e.DepartamentoID = d.DepartamentoID;

SELECT 
    c.ClaseID,
    cu.Nombre AS Curso,
    p.Nombre AS Profesor,
    c.Periodo
FROM Clase c
JOIN Curso cu ON c.CursoID = cu.CursoID
JOIN Profesor p ON c.ProfesorID = p.ProfesorID;

SELECT 
    e.Nombre AS Estudiante,
    cu.Nombre AS Curso,
    ca.Nota
FROM Calificacion ca
JOIN Inscripcion i ON ca.InscripcionID = i.InscripcionID
JOIN Estudiante e ON i.EstudianteID = e.EstudianteID
JOIN Clase cl ON i.ClaseID = cl.ClaseID
JOIN Curso cu ON cl.CursoID = cu.CursoID;

SELECT 
    p.Nombre AS Profesor,
    d.Nombre AS Departamento
FROM Profesor p
JOIN Departamento d ON p.DepartamentoID = d.DepartamentoID;

SELECT 
    cl.ClaseID,
    cu.Nombre AS Curso,
    COUNT(i.InscripcionID) AS TotalEstudiantes
FROM Clase cl
JOIN Curso cu ON cl.CursoID = cu.CursoID
JOIN Inscripcion i ON cl.ClaseID = i.ClaseID
GROUP BY cl.ClaseID;

SELECT COUNT(*) AS TotalEstudiantes
FROM Estudiante;
SELECT COUNT(*) AS TotalProfesores
FROM Profesor;
SELECT 
    d.Nombre AS Departamento,
    COUNT(e.EstudianteID) AS CantidadEstudiantes
FROM Departamento d
LEFT JOIN Estudiante e ON d.DepartamentoID = e.DepartamentoID
GROUP BY d.DepartamentoID;
SELECT MAX(Nota) AS NotaMaxima
FROM Calificacion;
SELECT MIN(Nota) AS NotaMinima
FROM Calificacion;












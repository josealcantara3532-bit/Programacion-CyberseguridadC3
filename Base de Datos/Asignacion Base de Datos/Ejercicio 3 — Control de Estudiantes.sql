CREATE DATABASE colegio;
USE colegio;

CREATE TABLE estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT
);

CREATE TABLE cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    nivel VARCHAR(50)
);

CREATE TABLE matriculas (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    id_curso INT,
    fecha DATE,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante),
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
);

INSERT INTO estudiantes (nombre, edad) VALUES
('Luis Gómez', 16),
('Ana Martínez', 17),
('Pedro Rodríguez', 15);

INSERT INTO cursos (nombre, nivel) VALUES
('Matemáticas', 'Intermedio'),
('Inglés', 'Básico'),
('Programación', 'Avanzado');

INSERT INTO matriculas (id_estudiante, id_curso, fecha) VALUES
(1, 1, '2025-02-10'),
(2, 3, '2025-02-11'),
(3, 2, '2025-02-12');

SELECT e.nombre AS estudiante, c.nombre AS curso, c.nivel, m.fecha
FROM matriculas m
JOIN estudiantes e ON m.id_estudiante = e.id_estudiante
JOIN cursos c ON m.id_curso = c.id_curso;

SELECT c.nombre, COUNT(m.id_estudiante) AS cantidad_estudiantes
FROM cursos c
LEFT JOIN matriculas m ON c.id_curso = m.id_curso
GROUP BY c.nombre;

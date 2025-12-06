CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE autores (
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50)
);

CREATE TABLE libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    año_publicacion INT,
    id_autor INT,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
);

INSERT INTO autores (nombre, nacionalidad) VALUES
('Gabriel García Márquez', 'Colombiana'),
('Isabel Allende', 'Chilena'),
('Mario Vargas Llosa', 'Peruana');

INSERT INTO libros (titulo, año_publicacion, id_autor) VALUES
('Cien Años de Soledad', 1967, 1),
('La Casa de los Espíritus', 1982, 2),
('La Ciudad y Los Perros', 1963, 3);

SELECT libros.titulo, autores.nombre
FROM libros
INNER JOIN autores ON libros.id_autor = autores.id_autor;

SELECT * FROM autores WHERE nacionalidad = 'Colombiana';

SELECT * FROM libros WHERE año_publicacion > 1970;



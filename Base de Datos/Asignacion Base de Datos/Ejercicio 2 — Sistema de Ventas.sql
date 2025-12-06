CREATE DATABASE ventas;
USE ventas;

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    telefono VARCHAR(20)
);

CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2)
);

CREATE TABLE facturas (
    id_factura INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_producto INT,
    cantidad INT,
    fecha DATE,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

INSERT INTO clientes (nombre, telefono) VALUES
('Juan Pérez', '809-555-1234'),
('María López', '829-777-9999');

INSERT INTO productos (nombre, precio) VALUES
('Laptop', 750.00),
('Mouse', 15.00),
('Monitor', 120.00);

INSERT INTO facturas (id_cliente, id_producto, cantidad, fecha) VALUES
(1, 1, 1, '2025-01-15'),
(1, 2, 2, '2025-01-15'),
(2, 3, 1, '2025-02-01');

SELECT f.id_factura, c.nombre AS cliente, p.nombre AS producto, f.cantidad, f.fecha
FROM facturas f
INNER JOIN clientes c ON f.id_cliente = c.id_cliente
INNER JOIN productos p ON f.id_producto = p.id_producto;

SELECT c.nombre, SUM(p.precio * f.cantidad) AS total_comprado
FROM facturas f
JOIN clientes c ON f.id_cliente = c.id_cliente
JOIN productos p ON f.id_producto = p.id_producto
GROUP BY c.nombre;



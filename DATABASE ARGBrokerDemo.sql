CREATE DATABASE ARGBrokerDemo;

USE ARGBrokerDemo;

CREATE TABLE PerfilesInversor(
id_perfil INT PRIMARY KEY,
tipo_inversor VARCHAR(50)
);
CREATE TABLE Provincias(
id_provincia INT PRIMARY KEY,
nombre_provincia VARCHAR(50));
CREATE TABLE Localidades(
id_localidad INT PRIMARY KEY,
nombre_localidad VARCHAR(50));
CREATE TABLE Inversores(
id_inversor INT PRIMARY KEY,
id_perfil INT,
id_localidad INT,
id_billetera INT,
nombre VARCHAR(70),
ex_plitica VARCHAR(2),
calle VARCHAR(70),
numero_calle INT,
correo_electronico VARCHAR(70),
contraseña VARCHAR(50));
CREATE TABLE Billeteras(
id_billetera INT PRIMARY KEY,
id_inversor INT,
id_operacion INT,
cantidad_accion_total INT,
valor_promedio FLOAT,
saldo_ars FLOAT,
balance_total FLOAT,
pnl FLOAT);
CREATE TABLE Operaciones(
id_operacion INT PRIMARY KEY,
tipo_operacion VARCHAR(30),
precio_operacion FLOAT,
cantidad_accion INT,
fecha DATETIME,
id_billetera INT,
id_accion INT,
monto_comision FLOAT);
CREATE TABLE Acciones(
id_accion INT PRIMARY KEY,
nombre_empresa VARCHAR(70),
monto_ultimo_operado FLOAT,
volumen_compra_diaria INT,
volumen_venta_diaria INT,
precio_compra FLOAT,
precio_venta FLOAT,
precio_apertura FLOAT,
min_diario FLOAT,
max_diario FLOAT, 
ultimo_cierre FLOAT);






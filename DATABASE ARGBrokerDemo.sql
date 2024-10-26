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
id_accion VARCHAR (50) PRIMARY KEY,
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

INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre) VALUES ("YPFD","YPF SOCIEDAD ANONIMA",299500000,530752,398064,29950,29351.0,27883.45,27883.45,29964.975,28452.5);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("GGAL","GRUPO FINANCIERO GALICIA SA",62900000,2194000,1645500,6290,6164.2,5855.99,5855.99,6293.145,5975.5);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("BMA","BANCO MACRO S.A.",92500000,517186,387889.5,9250,9065.0,8611.75,8611.75,9254.625,8787.5);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("PAMP","PAMPA ENERGIA S.A.",32000000,1365000,1023750,3200,3136.0,2979.2,2979.2,3201.6,3040.00);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("TECO2","TELECOM ARGENTINA SA",20150000,205971,154478.25,2015,1974.7,1875.965,1875.965,2016.0075,1914.25);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("TGSU2","TRANSPORTADORA DE GAS DEL SUR S.A",51900000,236038,177028.5,5190,5086.2,4831.89,4831.89,5192.595,4930.5);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("TXAR1","TERNIUM ARGENTINA SA",7900000,1422000,1066500,790,774.2,735.49,735.49,790.395,750.5);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("BBAR","BBVA BANCO FRANCES",52100000,705960,529470,5210,5105.8,4850.51,4850.51,5212.605,4949.5);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("ALUA","ALUAR ALUMINIO ARGENTINA SA",8170000,1159000,869250,817,800.66,760627,760.627,817.4085,776.15);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("CEPU","CENTRAL PUERTO SA",13050000,1132000,849000,1305,1278.9,1214.955,1214.955,1305.6525,1239.75);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("EDN","EMPRESA DISTR Y COMERC NORTE EDENOR",15400000,865285,648963.75,1540,1509.2,1433.74,1433.74,1540.77,1463.00);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("LOMA","LOMA NEGRA CIA IND ARGENTINA SA",21500000,768646,576484.5,2150,2107.0,2001.65,2001.65,2151.075,2042.5);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("BYMA","BOLSAS Y MERCADOS ARGENTINOS SA",3190000,2835000,2126250,319,312.62,296.989,296.989,319.1595,303.05);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("SUPV","GRUPO SUPERVIELLE S.A",20450000,737059,552794.25,2045,2004.1,1903.895,1903.895,2046.0225,1942.75);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("CVH","CABLEVISION HOLDING SA",48000000,8769,6576.75,4800,4704.0,4468.38,4468.8,4802.4,4560.00);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("COME","SOCIEDAD COMERCIAL DEL PLATA",2515000,4724000,3543000,251.5,246.47,234.1465,234.1465,251.62575,238.92500);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("TRAN","CIA DE TRANSP DE ENERGIA ELECTRICA",18450000,225960,169470,1845,1808.1,1717.695,1717.695,1845.9225,1752.75);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("HARG","HOLCIM (ARGENTINA) S.A",19600000,47566,35674.5,1960,1920.8,1824.76,1824.76,1960.98,1862);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("CRES","CRESUD S.A.C.I.F.Y.A.",11150000,737297,552972.75,1115,1092.7,1038065,1038.065,1115.5575,1059.25);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("MIRG","MIRGOR S.A.COMERC INDUST FINANC",222250000,2731,2048.25,22225,21780.5,20691.475,20691.475,22236.1125,21113.75);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("VALO","BANCO DE VALORES S.A.",3315000,2439000,1829250,331.5,324.87,308.6265,308.6265,331.66575,314.925);
INSERT INTO Acciones  (id_accion,nombre_empresa,monto_ultimo_operado,volumen_compra_diaria,volumen_venta_diaria,precio_compra,precio_venta,precio_apertura,min_diario,max_diario,ultimo_cierre)VALUES("TGNO4","TRANSPORTADORA DE GAS DEL NORTE S.A",30050000,309991,232493.acciones25,3005,2944.9,2797.655,2797.655,3006.5025,2854.75);

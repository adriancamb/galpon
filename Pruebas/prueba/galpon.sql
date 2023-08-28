--
-- File generated with SQLiteStudio v3.3.3 on do. abr. 2 20:48:02 2023
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: categorias
CREATE TABLE categorias (
    id          INTEGER PRIMARY KEY,
    nombre      TEXT,
    url         TEXT,
    imagen      TEXT,
    descripcion TEXT
);
INSERT INTO categorias (id, nombre, url, imagen, descripcion) VALUES (1, 'Jardí­n', 'productos/jardin.html', 'img/imagen.jpg', 'Esta es la descripcion');
INSERT INTO categorias (id, nombre, url, imagen, descripcion) VALUES (2, 'Parrillas', 'productos/parrillas.html', 'img/imagen.jpg', 'Esta es la descripcion');
INSERT INTO categorias (id, nombre, url, imagen, descripcion) VALUES (3, 'Calefacción', 'productos/calefaccion.html', 'img/imagen.jpg', 'Esta es la descripcion');
INSERT INTO categorias (id, nombre, url, imagen, descripcion) VALUES (4, 'Iluminación', 'productos/iluminacion.html', 'img/imagen.jpg', 'Esta es la descripcion');
INSERT INTO categorias (id, nombre, url, imagen, descripcion) VALUES (5, 'Gastronomí­a', 'productos/gastronomia.html', 'img/imagen.jpg', 'Esta es la descripcion');

-- Table: subcategorias
CREATE TABLE subcategorias (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre       TEXT    NOT NULL,
    url          TEXT    NOT NULL,
    imagen       TEXT    NOT NULL,
    descripcion  TEXT,
    destacado    INTEGER DEFAULT 0,
    id_categoria INTEGER REFERENCES categorias (id) 
);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (1, 'Arrollamangueras', 'productos/arrollamangueras.html', 'img/arrollamanguera.jpg', 'Arrollamanguera de distintos tipos', 1, 1);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (2, 'Bebederos', 'productos/bebederos.html', 'img/imagen.jpg', 'Esta es la descripcion', 1, 1);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (3, 'Llamadores', 'productos/llamadores.html', 'img/imagen.jpg', 'Esta es la descripcion', 1, 1);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (4, 'Veletas', 'productos/veletas.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 1);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (5, 'Muebles de Jardín', 'productos/muebles-de-jardin.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 1);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (6, 'Accesorios para parrillas', 'productos/accesorios-para-parrillas.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 2);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (7, 'Asadores', 'productos/asadores.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 2);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (8, 'Herrajes', 'productos/herrajes.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 2);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (9, 'Parrillas a carbón o leña', 'productos/parrillas-a-carbon-o-lena.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 2);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (10, 'Parrillas a gas', 'productos/parrillas-a-gas.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 2);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (11, 'Hogares', 'productos/hogares.html', 'img/imagen.jpg', 'Esta es la descripción', 0, 3);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (12, 'Faroles', 'productos/faroles.html', 'img/imagen.jpg', 'Esta es la descripción', 0, 4);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (13, 'Faroles con columnas', 'productos/faroles-con-columnas.html', 'img/imagen.jpg', 'Esta es la descripción', 0, 4);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (14, 'Calderos en hierro', 'productos/calderos-en-hierro.html', 'img/calderos-en-hierro.jpg', 'calderos-en-hierro', 0, 5);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (15, 'Calcerolas de fundicion', 'productos/cacerolas-de-fundicion.html', 'img/cacerolas-de-fundicion.jpg', 'cacerolas-de-fundicion', 0, 5);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (16, 'Planchas para bifes', 'productos/planchas-para-bifes.html', 'img/planchas-para-bifes.jpg', 'planchas-para-bifes', 0, 5);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (17, 'Provoleteras de fundicion', 'productos/provoleteras.html', 'img/provoleteras.html', 'provoleteras', 0, 5);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (18, 'Asaderas en chapa plegada', 'productos/asaderas-en-chapa-plegada.html', 'img/asaderas-en-chapa-plegada.jpg', 'asaderas-en-chapa-plegada', 0, 5);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (19, 'Paelleras con 2 asas', 'productos/paelleras-con-2-asas.html', 'img/paelleras-con-2-asas.jpg', 'paelleras-con-2-asas', 0, 5);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (20, 'Woks', 'productos/woks.html', 'img/woks.jpg', 'woks', 0, 5);
INSERT INTO subcategorias (id, nombre, url, imagen, descripcion, destacado, id_categoria) VALUES (21, 'Pizzera en chapa enlozada', 'productos/pizzera-en-chapa-enlozada.html', 'img/pizzera-en-chapa-enlozada.jpg', 'pizzera-en-chapa-enlozada', 0, 5);

-- Table: subcategorias2
CREATE TABLE subcategorias2 (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre       TEXT    NOT NULL,
    url          TEXT    NOT NULL,
    imagen       TEXT    NOT NULL,
    descripcion  TEXT,
    destacado    INTEGER DEFAULT 0,
    id_subcategoria INTEGER REFERENCES subcategorias (id) 
);
INSERT INTO subcategorias2 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria) VALUES (1, 'Fundición de aluminio', 'productos/fundicion-de-aluminio.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 5);
INSERT INTO subcategorias2 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria) VALUES (2, 'Función de hierro', 'productos/funcion-de-hierro.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 5);
INSERT INTO subcategorias2 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria) VALUES (3, 'Hierro forjado', 'productos/hierro-forjado.html', 'img/imagen.jpg', 'Esta es la descripcion', 0, 5);
INSERT INTO subcategorias2 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria) VALUES (4, 'Enlonzadas', 'productos/cacerolas-de-fundicion-enlonzadas.html', 'img/cacerolas-de-fundicion-enlonzadas.jpg', 'cacerolas-de-fundicion-enlozadas', 0, 15);
INSERT INTO subcategorias2 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria) VALUES (5, 'Sin enlonzar', 'productos/cacerolas-de-fundicion-sin-enlonzar.html', 'img/cacerolas-de-fundicion-sin-enlonzar.jpg', 'cacerolas-de-fundicion-sin-enlozar', 0, 15);
INSERT INTO subcategorias2 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria) VALUES (6, 'Lisas', 'productos/planchas-para-bifes-lisas.html', 'img/planchas-para-bifes-lisas.jpg', 'planchas-para-bifes-lisas', 0, 16);
INSERT INTO subcategorias2 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria) VALUES (7, 'Rayadas', 'productos/planchas-para-bifes-rayadas.html', 'img/planchas-para-bifes-rayadas.jpg', 'planchas-para-bifes-rayadas', 0, 16);
INSERT INTO subcategorias2 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria) VALUES (8, 'Mangos de madera', 'productos/provoleteras-mango-de-madera.html', 'img/provoleteras-mango-de-madera.html', 'provoleteras-mango-de-madera', 0, 17);
INSERT INTO subcategorias2 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria) VALUES (9, 'Mangos de fundicion', 'productos/provoleteras-mango-de-fundicion.html', 'img/provoleteras-mango-de-fundicion.jpg', 'provoleteras-mango-de-fundicion', 0, 17);
INSERT INTO subcategorias2 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria) VALUES (10, 'De 15 porciones', 'productos/provoleteras-15-porciones.html', 'img/provoleteras-15-porciones.jpg', 'provoleteras-15-porciones', 0, 17);
INSERT INTO subcategorias2 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria) VALUES (11, 'Enlonzadas', 'productos/paelleras-con-2-asas-enlozadas.html', 'img/paelleras-con-2-asas-enlonzadas.jpg', 'paelleras-con-2-asas-enlozadas', 0, 19);
INSERT INTO subcategorias2 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria) VALUES (12, 'Sin enlonzar', 'productos/paelleras-con-2-asas-sin-enlonzar.html', 'img/paelleras-con-2-asas-sin-enlonzar.jpg', 'paelleras-con-2-asas-sin-enlozar', 0, 19);
INSERT INTO subcategorias2 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria) VALUES (13, 'Enlonzados', 'productos/woks-enlozados.html', 'img/woks-enlonzados.jpg', 'woks-enlozados', 0, 20);
INSERT INTO subcategorias2 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria) VALUES (14, 'Sin enlonzar', 'productos/woks-sin-enlonzar.html', 'img/woks-sin-enlonzar.jpg', 'woks-sin-enlozar', 0, 20);

-- Table: subcategorias3
CREATE TABLE subcategorias3 (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre       TEXT    NOT NULL,
    url          TEXT    NOT NULL,
    imagen       TEXT    NOT NULL,
    descripcion  TEXT,
    destacado    INTEGER DEFAULT 0,
    id_subcategoria2 INTEGER REFERENCES subcategorias2 (id) 
);
INSERT INTO subcategorias3 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria2) VALUES (1, 'Ovaladas', 'productos/cacerolas-de-fundicion-sin-enlonzar-ovaladas.html', 'img/cacerolas-de-fundicion-sin-enlonzar-ovaladas.jpg', 'cacerolas-de-fundicion-sin-enlozar-ovaladas', 0, 5);
INSERT INTO subcategorias3 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria2) VALUES (2, 'Enlonzadas', 'productos/planchas-para-bifes-rayadas-enlozadas.html', 'img/planchas-para-bifes-rayadas-enlozadas.jpg', 'planchas-para-bifes-rayadas-enlozadas', 0, 7);
INSERT INTO subcategorias3 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria2) VALUES (3, 'Sin enlonzar', 'productos/planchas-para-bifes-rayadas-sin-enlozar.html', 'img/planchas-para-bifes-rayadas-sin-enlozar.jpg', 'planchas-para-bifes-rayadas-sin-enlozar', 0, 7);
INSERT INTO subcategorias3 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria2) VALUES (4, 'Enlonzadas', 'productos/provoleteras-enlonzadas.html', 'img/provoleteras-enlonzadas.jpg', 'provoleteras-enlozadas', 0, 8);
INSERT INTO subcategorias3 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria2) VALUES (5, 'Sin enlonzar', 'productos/provoleteras-sin-enlonzar.html', 'img/provoleteras-sin-enlonzar.jpg', 'provoleteras-sin-enlozar', 0, 8);
INSERT INTO subcategorias3 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria2) VALUES (6, 'Enlonzadas', 'productos/provoleteras-enlonzadas.html', 'img/provoleteras-enlonzadas.jpg', 'provoleteras-enlozadas', 0, 9);
INSERT INTO subcategorias3 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria2) VALUES (7, 'Sin enlonzar', 'productos/provoleteras-sin-enlonzar.html', 'img/provoleteras-sin-enlonzar.jpg', 'provoleteras-sin-enlozar', 0, 9);
INSERT INTO subcategorias3 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria2) VALUES (8, 'Enlonzadas', 'productos/provoleteras-15-porciones-enlozadas.html', 'img/provoletera-15-porcioness-enlonzadas.jpg', 'provoleteras-15-porciones-enlozadas', 0, 10);
INSERT INTO subcategorias3 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria2) VALUES (9, 'Sin enlonzar', 'productos/provoleteras-15-porciones-sin-enlonzar.html', 'img/provoleteras-15-porciones-sin-enlonzar.jpg', 'provoleteras-15-porciones-sin-enlozar', 0, 10);

-- Table: subcategorias4
CREATE TABLE subcategorias4 (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre       TEXT    NOT NULL,
    url          TEXT    NOT NULL,
    imagen       TEXT    NOT NULL,
    descripcion  TEXT,
    destacado    INTEGER DEFAULT 0,
    id_subcategoria3 INTEGER REFERENCES subcategorias3 (id) 
);
INSERT INTO subcategorias4 (id, nombre, url, imagen, descripcion, destacado, id_subcategoria3) VALUES (1, 'Doble función', 'productos/cacerolas-de-fundicion-sin-enlonzar-ovaladas-doble-funcion.html', 'img/cacerolas-de-fundicion-sin-enlonzar-ovaladas-doble-funcion.jpg', 'cacerolas-de-fundicion-sin-enlozar-ovaladas-doble-funcion', 0, 1);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

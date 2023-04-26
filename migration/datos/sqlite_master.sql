insert into main.sqlite_master (type, name, tbl_name, rootpage, sql)
values  ('table', 'sqlite_sequence', 'sqlite_sequence', 3, 'CREATE TABLE sqlite_sequence(name,seq)'),
        ('table', 'CATEGORIA_INGREDIENTE', 'CATEGORIA_INGREDIENTE', 6, 'CREATE TABLE CATEGORIA_INGREDIENTE
(
	id_categoria INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre_categoria TEXT NOT NULL COLLATE NOCASE
)'),
        ('table', 'CORREO', 'CORREO', 7, 'CREATE TABLE CORREO
(
	id_correo INTEGER NOT NULL PRIMARY KEY,
	correo TEXT NOT NULL COLLATE NOCASE,
	id_usuario INTEGER NOT NULL,
	CONSTRAINT FK_CORREO_USUARIO FOREIGN KEY (id_usuario) REFERENCES USUARIO (id_usuario) ON DELETE No Action ON UPDATE No Action,
	CONSTRAINT CH_CORREO CHECK (
	    correo LIKE ''%_@_%._%'' AND
	    LENGTH(correo) - LENGTH(REPLACE(correo, ''@'', '''')) = 1 AND
	    SUBSTR(LOWER(correo), 1, INSTR(correo, ''.'') - 1) NOT GLOB ''*[^@0-9a-z]*'' AND
	    SUBSTR(LOWER(correo), INSTR(correo, ''.'') + 1) NOT GLOB ''*[^a-z]*''
	  )
)'),
        ('table', 'ENFERMEDAD', 'ENFERMEDAD', 8, 'CREATE TABLE ENFERMEDAD
(
	id_enfermedad INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre_enfermedad TEXT NOT NULL COLLATE NOCASE
)'),
        ('table', 'ENFERMEDAD_USUARIO', 'ENFERMEDAD_USUARIO', 9, 'CREATE TABLE ENFERMEDAD_USUARIO
(
	id_usuario INTEGER NOT NULL,
	id_enfermedad INTEGER NOT NULL,
	CONSTRAINT PK_ENFERMEDAD_USUARIO PRIMARY KEY (id_usuario,id_enfermedad),
	CONSTRAINT FK_ENFERMEDAD_USUARIO FOREIGN KEY (id_usuario) REFERENCES USUARIO (id_usuario) ON DELETE No Action ON UPDATE No Action,
	CONSTRAINT FK_ENFERMEDAD_USUARIO_ENFERMEDADES FOREIGN KEY (id_enfermedad) REFERENCES ENFERMEDAD (id_enfermedad) ON DELETE No Action ON UPDATE No Action
)'),
        ('index', 'sqlite_autoindex_ENFERMEDAD_USUARIO_1', 'ENFERMEDAD_USUARIO', 10, null),
        ('table', 'ESTATURA', 'ESTATURA', 11, 'CREATE TABLE ESTATURA
(
	id_estatura INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	estatura INTEGER NOT NULL,
	fecha_toma TEXT NOT NULL COLLATE NOCASE,
	id_usuario INTEGER NOT NULL,
	CONSTRAINT FK_ESTATURA_USUARIO FOREIGN KEY (id_usuario) REFERENCES USUARIO (id_usuario) ON DELETE No Action ON UPDATE No Action,
	CONSTRAINT CH_ESTATURA CHECK (estatura > 100 and estatura < 400)
)'),
        ('table', 'ESTILO_VIDA', 'ESTILO_VIDA', 12, 'CREATE TABLE ESTILO_VIDA
(
	id_estilo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre_estilo TEXT NOT NULL COLLATE NOCASE
)'),
        ('table', 'INGREDIENTE', 'INGREDIENTE', 13, 'CREATE TABLE INGREDIENTE
(
	id_ingrediente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre_ingrediente TEXT NOT NULL COLLATE NOCASE,
	cantidad_calorias REAL NOT NULL,
	id_categoria INTEGER NOT NULL,
	CONSTRAINT FK_INGREDIENTE_CATEGORIA_INGREDIENTE FOREIGN KEY (id_categoria) REFERENCES CATEGORIA_INGREDIENTE (id_categoria) ON DELETE No Action ON UPDATE No Action
)'),
        ('table', 'PESO', 'PESO', 16, 'CREATE TABLE PESO
(
	id_peso INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	peso REAL NOT NULL,
	fecha_toma TEXT NOT NULL COLLATE NOCASE,
	id_usuario INTEGER NOT NULL,
	CONSTRAINT FK_PESO_USUARIO FOREIGN KEY (id_usuario) REFERENCES USUARIO (id_usuario) ON DELETE No Action ON UPDATE No Action,
	CONSTRAINT CH_PESO CHECK(peso>30 and peso<400)
)'),
        ('index', 'IXFK_CORREO_USUARIO', 'CORREO', 28, 'CREATE INDEX IXFK_CORREO_USUARIO
 ON CORREO (id_usuario ASC)
'),
        ('index', 'IXFK_ENFERMEDAD_USUARIO', 'ENFERMEDAD_USUARIO', 29, 'CREATE INDEX IXFK_ENFERMEDAD_USUARIO
 ON ENFERMEDAD_USUARIO (id_usuario ASC)
'),
        ('index', 'IXFK_ENFERMEDAD_USUARIO_ENFERMEDADES', 'ENFERMEDAD_USUARIO', 30, 'CREATE INDEX IXFK_ENFERMEDAD_USUARIO_ENFERMEDADES
 ON ENFERMEDAD_USUARIO (id_enfermedad ASC)
'),
        ('index', 'IXFK_ESTATURA_USUARIO', 'ESTATURA', 31, 'CREATE INDEX IXFK_ESTATURA_USUARIO
 ON ESTATURA (id_usuario ASC)
'),
        ('index', 'IXFK_INGREDIENTE_CATEGORIA_INGREDIENTE', 'INGREDIENTE', 32, 'CREATE INDEX IXFK_INGREDIENTE_CATEGORIA_INGREDIENTE
 ON INGREDIENTE (id_categoria ASC)
'),
        ('index', 'IXFK_PESO_USUARIO', 'PESO', 35, 'CREATE INDEX IXFK_PESO_USUARIO
 ON PESO (id_usuario ASC)
'),
        ('table', 'USUARIO', 'USUARIO', 62, 'CREATE TABLE "USUARIO" (
	"id_usuario"	INTEGER NOT NULL,
	"nombre_usuario"	TEXT NOT NULL COLLATE NOCASE,
	"fecha_nacimiento"	TEXT NOT NULL COLLATE NOCASE,
	"id_estilo_vida"	INTEGER NOT NULL,
	PRIMARY KEY("id_usuario" AUTOINCREMENT),
	CONSTRAINT "FK_USUARIO_ESTILO_VIDA" FOREIGN KEY("id_estilo_vida") REFERENCES "ESTILO_VIDA"("id_estilo") ON DELETE No Action ON UPDATE No Action
)'),
        ('index', 'IXFK_USUARIO_ESTILO_VIDA', 'USUARIO', 25, 'CREATE INDEX "IXFK_USUARIO_ESTILO_VIDA" ON "USUARIO" (
	"id_estilo_vida"	ASC
)'),
        ('view', 'ULTIMO_PESO', 'ULTIMO_PESO', 0, 'CREATE VIEW ULTIMO_PESO
AS
    SELECT U.nombre_usuario,P.fecha_toma,P.peso
    FROM USUARIO U
    JOIN PESO P ON U.id_usuario = P.id_usuario
    WHERE P.fecha_toma=(SELECT MAX(fecha_toma) FROM PESO pe WHERE P.id_usuario=pe.id_usuario)'),
        ('view', 'ULTIMA_ESTATURA', 'ULTIMA_ESTATURA', 0, 'CREATE VIEW ULTIMA_ESTATURA
AS
    SELECT U.nombre_usuario,E.fecha_toma,E.estatura
    FROM USUARIO U
    JOIN ESTATURA E ON U.id_usuario = E.id_usuario
    WHERE E.fecha_toma=(SELECT MAX(fecha_toma) FROM ESTATURA es WHERE E.id_usuario=es.id_usuario)'),
        ('table', 'RECETA', 'RECETA', 2, 'CREATE TABLE RECETA
(
    id_receta INTEGER not null
        primary key autoincrement,
    nombre_receta TEXT collate NOCASE not null,
    tipo_comida TEXT not null, preparacion TEXT not null,
    CHECK (tipo_comida IN (''Desayuno'',''Almuerzo'',''Cena'',''Merienda''))
)'),
        ('table', 'OBJETIVO', 'OBJETIVO', 19, 'CREATE TABLE OBJETIVO(
    id_objetivo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
    nombre_objetivo TEXT NOT NULL
)'),
        ('table', 'RUTINA', 'RUTINA', 22, 'CREATE TABLE RUTINA
(
    id_rutina        INTEGER not null
        primary key autoincrement,
    cantidad_comidas INTEGER not null,
    id_objetivo      INTEGER not null
        constraint FK_RUTINA_OBJETIVO
            references OBJETIVO
)'),
        ('index', 'IXFK_RUTINA_OBJETIVO_RUTINA', 'RUTINA', 26, 'CREATE INDEX IXFK_RUTINA_OBJETIVO_RUTINA
    on RUTINA (id_objetivo)'),
        ('table', 'RECETA_RUTINA', 'RECETA_RUTINA', 20, 'CREATE TABLE RECETA_RUTINA
(
    id_rutina             INTEGER not null
        constraint FK_RECETA_RUTINA_RUTINA
            references RUTINA,
    id_receta             INTEGER not null
        constraint FK_RECETA_RUTINA_RECETA
            references RECETA,
    constraint PK_RECETA_RUTINA
        primary key (id_rutina, id_receta)
)'),
        ('index', 'sqlite_autoindex_RECETA_RUTINA_1', 'RECETA_RUTINA', 21, null),
        ('index', 'IXFK_RECETA_RUTINA_RECETA', 'RECETA_RUTINA', 36, 'CREATE INDEX IXFK_RECETA_RUTINA_RECETA
    on RECETA_RUTINA (id_receta)'),
        ('index', 'IXFK_RECETA_RUTINA_RUTINA', 'RECETA_RUTINA', 37, 'CREATE INDEX IXFK_RECETA_RUTINA_RUTINA
    on RECETA_RUTINA (id_rutina)'),
        ('table', 'RUTINA_USUARIO', 'RUTINA_USUARIO', 23, 'CREATE TABLE RUTINA_USUARIO
(
    id_usuario       INTEGER not null
        constraint FK_RUTINA_USUARIO_USUARIO
            references USUARIO,
    id_rutina        INTEGER not null
        constraint FK_RUTINA_USUARIO_RUTINA
            references RUTINA,
    calorias_diarias integer not null,
    vigente          integer,
    constraint PK_RUTINA_USUARIO
        primary key (id_usuario, id_rutina),
    CHECK(vigente in (1,0))
)'),
        ('index', 'sqlite_autoindex_RUTINA_USUARIO_1', 'RUTINA_USUARIO', 24, null),
        ('index', 'IXFK_RUTINA_USARIO_RUTINA', 'RUTINA_USUARIO', 38, 'CREATE INDEX IXFK_RUTINA_USARIO_RUTINA
    on RUTINA_USUARIO (id_rutina)'),
        ('index', 'IXFK_RUTINA_USUARIO_USUARIO', 'RUTINA_USUARIO', 39, 'CREATE INDEX IXFK_RUTINA_USUARIO_USUARIO
    on RUTINA_USUARIO (id_usuario)'),
        ('table', 'ABANDONO', 'ABANDONO', 27, 'CREATE TABLE ABANDONO(
    id_abandono INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_rutina INTEGER NOT NULL CONSTRAINT FK_ABANDONO_RUTINA REFERENCES RUTINA,
    id_usuario INTEGER NOT NULL CONSTRAINT FK_ABANDONO_USUARIO REFERENCES USUARIO,
    finalizado INTEGER NOT NULL,
    motivo TEXT NOT NULL,
    CHECK (finalizado in (1,0))
)'),
        ('index', 'IXFK_ABANDONO_RUTINA_ABANDONO', 'ABANDONO', 66, 'CREATE INDEX IXFK_ABANDONO_RUTINA_ABANDONO
    on ABANDONO (id_rutina)'),
        ('index', 'IXFK_ABANDONO_USUARIO_ABANDONO', 'ABANDONO', 67, 'CREATE INDEX IXFK_ABANDONO_USUARIO_ABANDONO
    on ABANDONO (id_usuario)'),
        ('table', 'INGREDIENTE_RECETA', 'INGREDIENTE_RECETA', 68, 'CREATE TABLE "INGREDIENTE_RECETA"
(
    id_receta            INTEGER not null
        constraint FK_INGREDIENTE_RECETA_RECETA
            references RECETA,
    id_ingrediente       INTEGER not null
        constraint FK_INGREDIENTE_RECETA_INGREDIENTE
            references INGREDIENTE,
    cantidad_ingrediente REAL    not null,
    constraint PK_INGREDIENTE_RECETA
        primary key (id_receta, id_ingrediente)
)'),
        ('index', 'sqlite_autoindex_INGREDIENTE_RECETA_1', 'INGREDIENTE_RECETA', 69, null),
        ('index', 'IXFK_INGREDIENTE_RECETA_INGREDIENTE', 'INGREDIENTE_RECETA', 14, 'CREATE INDEX IXFK_INGREDIENTE_RECETA_INGREDIENTE
    on INGREDIENTE_RECETA (id_ingrediente)'),
        ('index', 'IXFK_INGREDIENTE_RECETA_RECETA', 'INGREDIENTE_RECETA', 15, 'CREATE INDEX IXFK_INGREDIENTE_RECETA_RECETA
    on INGREDIENTE_RECETA (id_receta)'),
        ('view', 'RECETA_CON_INGREDIENTES', 'RECETA_CON_INGREDIENTES', 0, 'CREATE VIEW RECETA_CON_INGREDIENTES
AS
SELECT nombre_receta,nombre_ingrediente,tipo_comida,preparacion,CEIL(cantidad_calorias*cantidad_ingrediente)calorias_ingrediente
        FROM RECETA re
        JOIN INGREDIENTE_RECETA IR ON re.id_receta = IR.id_receta
        JOIN INGREDIENTE I ON IR.id_ingrediente = I.id_ingrediente'),
        ('view', 'RESUMEN_RECETA', 'RESUMEN_RECETA', 0, 'CREATE VIEW RESUMEN_RECETA
AS
SELECT nombre_receta,tipo_comida,preparacion,sum(calorias_ingrediente) total_calorias
FROM RECETA_CON_INGREDIENTES
GROUP BY nombre_receta'),
        ('table', 'ALERGIA', 'ALERGIA', 33, 'CREATE TABLE "ALERGIA"
(
    id_usuario     INTEGER not null
        constraint FK_ALERGIA_USUARIO
            references USUARIO,
    id_ingrediente INTEGER not null
        constraint FK_ALERGIA_ALERGENO
            references INGREDIENTE (id_ingrediente),
    constraint PK_ALERGIA
        primary key (id_usuario, id_ingrediente)
)'),
        ('index', 'sqlite_autoindex_ALERGIA_1', 'ALERGIA', 34, null),
        ('index', 'IXFK_ALERGIA_ALERGENO', 'ALERGIA', 4, 'CREATE INDEX IXFK_ALERGIA_ALERGENO
    on ALERGIA (id_ingrediente)'),
        ('index', 'IXFK_ALERGIA_USUARIO', 'ALERGIA', 5, 'CREATE INDEX IXFK_ALERGIA_USUARIO
    on ALERGIA (id_usuario)');
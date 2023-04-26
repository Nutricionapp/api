create table if not exists CATEGORIA_INGREDIENTE
(
    id_categoria     INTEGER             not null
        primary key autoincrement,
    nombre_categoria TEXT collate NOCASE not null
);

create table if not exists ENFERMEDAD
(
    id_enfermedad     INTEGER             not null
        primary key autoincrement,
    nombre_enfermedad TEXT collate NOCASE not null
);

create table if not exists ESTILO_VIDA
(
    id_estilo     INTEGER             not null
        primary key autoincrement,
    nombre_estilo TEXT collate NOCASE not null
);

create table if not exists INGREDIENTE
(
    id_ingrediente     INTEGER             not null
        primary key autoincrement,
    nombre_ingrediente TEXT collate NOCASE not null,
    cantidad_calorias  REAL                not null,
    id_categoria       INTEGER             not null
        constraint FK_INGREDIENTE_CATEGORIA_INGREDIENTE
            references CATEGORIA_INGREDIENTE
);

create index IXFK_INGREDIENTE_CATEGORIA_INGREDIENTE
    on INGREDIENTE (id_categoria);

create table if not exists OBJETIVO
(
    id_objetivo     INTEGER not null
        primary key autoincrement,
    nombre_objetivo TEXT    not null
);

create table if not exists RECETA
(
    id_receta     INTEGER             not null
        primary key autoincrement,
    nombre_receta TEXT collate NOCASE not null,
    tipo_comida   TEXT                not null,
    preparacion   TEXT                not null,
    check (tipo_comida IN ('Desayuno', 'Almuerzo', 'Cena', 'Merienda'))
);

create table if not exists INGREDIENTE_RECETA
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
);

create index IXFK_INGREDIENTE_RECETA_INGREDIENTE
    on INGREDIENTE_RECETA (id_ingrediente);

create index IXFK_INGREDIENTE_RECETA_RECETA
    on INGREDIENTE_RECETA (id_receta);

create table if not exists RUTINA
(
    id_rutina        INTEGER not null
        primary key autoincrement,
    cantidad_comidas INTEGER not null,
    id_objetivo      INTEGER not null
        constraint FK_RUTINA_OBJETIVO
            references OBJETIVO
);

create table if not exists RECETA_RUTINA
(
    id_rutina INTEGER not null
        constraint FK_RECETA_RUTINA_RUTINA
            references RUTINA,
    id_receta INTEGER not null
        constraint FK_RECETA_RUTINA_RECETA
            references RECETA,
    constraint PK_RECETA_RUTINA
        primary key (id_rutina, id_receta)
);

create index IXFK_RECETA_RUTINA_RECETA
    on RECETA_RUTINA (id_receta);

create index IXFK_RECETA_RUTINA_RUTINA
    on RECETA_RUTINA (id_rutina);

create index IXFK_RUTINA_OBJETIVO_RUTINA
    on RUTINA (id_objetivo);

create table if not exists USUARIO
(
    id_usuario       INTEGER             not null
        primary key autoincrement,
    nombre_usuario   TEXT collate NOCASE not null,
    fecha_nacimiento TEXT collate NOCASE not null,
    id_estilo_vida   INTEGER             not null
        constraint FK_USUARIO_ESTILO_VIDA
            references ESTILO_VIDA
);

create table if not exists ABANDONO
(
    id_abandono INTEGER not null
        primary key autoincrement,
    id_rutina   INTEGER not null
        constraint FK_ABANDONO_RUTINA
            references RUTINA,
    id_usuario  INTEGER not null
        constraint FK_ABANDONO_USUARIO
            references USUARIO,
    finalizado  INTEGER not null,
    motivo      TEXT    not null,
    check (finalizado in (1, 0))
);

create index IXFK_ABANDONO_RUTINA_ABANDONO
    on ABANDONO (id_rutina);

create index IXFK_ABANDONO_USUARIO_ABANDONO
    on ABANDONO (id_usuario);

create table if not exists ALERGIA
(
    id_usuario     INTEGER not null
        constraint FK_ALERGIA_USUARIO
            references USUARIO,
    id_ingrediente INTEGER not null
        constraint FK_ALERGIA_ALERGENO
            references INGREDIENTE,
    constraint PK_ALERGIA
        primary key (id_usuario, id_ingrediente)
);

create index IXFK_ALERGIA_ALERGENO
    on ALERGIA (id_ingrediente);

create index IXFK_ALERGIA_USUARIO
    on ALERGIA (id_usuario);

create table if not exists CORREO
(
    id_correo  INTEGER             not null
        primary key,
    correo     TEXT collate NOCASE not null,
    id_usuario INTEGER             not null
        constraint FK_CORREO_USUARIO
            references USUARIO,
    constraint CH_CORREO
        check (correo LIKE '%_@_%._%' AND
               LENGTH(correo) - LENGTH(REPLACE(correo, '@', '')) = 1 AND
               SUBSTR(LOWER(correo), 1, INSTR(correo, '.') - 1) NOT GLOB '*[^@0-9a-z]*' AND
               SUBSTR(LOWER(correo), INSTR(correo, '.') + 1) NOT GLOB '*[^a-z]*')
);

create index IXFK_CORREO_USUARIO
    on CORREO (id_usuario);

create table if not exists ENFERMEDAD_USUARIO
(
    id_usuario    INTEGER not null
        constraint FK_ENFERMEDAD_USUARIO
            references USUARIO,
    id_enfermedad INTEGER not null
        constraint FK_ENFERMEDAD_USUARIO_ENFERMEDADES
            references ENFERMEDAD,
    constraint PK_ENFERMEDAD_USUARIO
        primary key (id_usuario, id_enfermedad)
);

create index IXFK_ENFERMEDAD_USUARIO
    on ENFERMEDAD_USUARIO (id_usuario);

create index IXFK_ENFERMEDAD_USUARIO_ENFERMEDADES
    on ENFERMEDAD_USUARIO (id_enfermedad);

create table if not exists ESTATURA
(
    id_estatura INTEGER             not null
        primary key autoincrement,
    estatura    INTEGER             not null,
    fecha_toma  TEXT collate NOCASE not null,
    id_usuario  INTEGER             not null
        constraint FK_ESTATURA_USUARIO
            references USUARIO,
    constraint CH_ESTATURA
        check (estatura > 100 and estatura < 400)
);

create index IXFK_ESTATURA_USUARIO
    on ESTATURA (id_usuario);

create table if not exists PESO
(
    id_peso    INTEGER             not null
        primary key autoincrement,
    peso       REAL                not null,
    fecha_toma TEXT collate NOCASE not null,
    id_usuario INTEGER             not null
        constraint FK_PESO_USUARIO
            references USUARIO,
    constraint CH_PESO
        check (peso > 30 and peso < 400)
);

create index IXFK_PESO_USUARIO
    on PESO (id_usuario);

create table if not exists RUTINA_USUARIO
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
    check (vigente in (1, 0))
);

create index IXFK_RUTINA_USARIO_RUTINA
    on RUTINA_USUARIO (id_rutina);

create index IXFK_RUTINA_USUARIO_USUARIO
    on RUTINA_USUARIO (id_usuario);

create index IXFK_USUARIO_ESTILO_VIDA
    on USUARIO (id_estilo_vida);

create view if not exists RECETA_CON_INGREDIENTES
AS
SELECT nombre_receta,nombre_ingrediente,tipo_comida,preparacion,CEIL(cantidad_calorias*cantidad_ingrediente)calorias_ingrediente
        FROM RECETA re
        JOIN INGREDIENTE_RECETA IR ON re.id_receta = IR.id_receta
        JOIN INGREDIENTE I ON IR.id_ingrediente = I.id_ingrediente;

create view if not exists RESUMEN_RECETA
AS
SELECT nombre_receta,tipo_comida,preparacion,sum(calorias_ingrediente) total_calorias
FROM RECETA_CON_INGREDIENTES
GROUP BY nombre_receta;

create view if not exists ULTIMA_ESTATURA
AS
    SELECT U.nombre_usuario,E.fecha_toma,E.estatura
    FROM USUARIO U
    JOIN ESTATURA E ON U.id_usuario = E.id_usuario
    WHERE E.fecha_toma=(SELECT MAX(fecha_toma) FROM ESTATURA es WHERE E.id_usuario=es.id_usuario);

create view if not exists ULTIMO_PESO
AS
    SELECT U.nombre_usuario,P.fecha_toma,P.peso
    FROM USUARIO U
    JOIN PESO P ON U.id_usuario = P.id_usuario
    WHERE P.fecha_toma=(SELECT MAX(fecha_toma) FROM PESO pe WHERE P.id_usuario=pe.id_usuario);



CREATE TABLE
	generos(
		id_genero INTEGER PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE
	estado_civiles(
		id_estado_civil INTEGER PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE
	ocupaciones(
		id_ocupacion INTEGER PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE personas (
    id_persona INTEGER PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    cedula VARCHAR(50),
    id_genero INTEGER NOT NULL,
    id_estado_civil INTEGER NOT NULL,
    id_ocupacion INTEGER NOT NULL,
    FOREIGN KEY(id_genero) REFERENCES generos(id_genero),
    FOREIGN KEY(id_estado_civil) REFERENCES estado_civiles(id_estado_civil),
    FOREIGN KEY(id_ocupacion) REFERENCES ocupaciones(id_ocupacion)
); 

CREATE TABLE
	enfermedades(
		id_enfermeda INTEGER PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE pacientes (
    id_paciente INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT NOT NULL CHECK (edad >= 0),  -- Asegura que la edad no sea negativa
    peso DECIMAL(5, 2) NOT NULL CHECK (peso >= 0),  -- Asegura que el peso no sea negativo
    altura DECIMAL(5, 2) NOT NULL CHECK (altura >= 0),  -- Asegura que la altura no sea negativa
    id_enfermeda INTEGER NOT NULL,
    FOREIGN KEY(id_enfermeda) REFERENCES enfermedades(id_enfermeda)
);

CREATE TABLE 
	dias(
		id_dia INTEGER PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);	

CREATE TABLE
	horas(
		id_hora INTEGER PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);		

CREATE TABLE
	turnos(
		id_turno INTEGER PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE medicos (
    id_medico INTEGER PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    especialidad VARCHAR(50),
    id_dia INTEGER NOT NULL,
    id_hora INTEGER NOT NULL,
    id_turno INTEGER NOT NULL,
    FOREIGN KEY(id_dia) REFERENCES dias(id_dia),
    FOREIGN KEY(id_hora) REFERENCES horas(id_hora),
    FOREIGN KEY(id_turno) REFERENCES turnos(id_turno)
);

CREATE TABLE
	servicios(
		id_servicio INTEGER PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE
	tipo_pagos(
		id_tipo_pago INTEGER PRIMARY KEY,
		descripcion varchar(60) UNIQUE,
        id_servicio INTEGER NOT NULL,
    FOREIGN KEY(id_servicio) REFERENCES servicios(id_servicio)
	);
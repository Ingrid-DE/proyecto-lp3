CREATE TABLE
	ciudades(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE
	personas(
		id serial PRIMARY KEY,
		descripcion varchar(60) UNIQUE,
		apellido varchar(50),
		numero_cedula decimal(8) UNIQUE,
		dirección varchar(50),
		numero_telefono decimal(9) UNIQUE,
		ocupacion varchar(60) UNIQUE,
		estado_civil varchar(60) UNIQUE
	);

CREATE TABLE
	medicos(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE
		pacientes(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);




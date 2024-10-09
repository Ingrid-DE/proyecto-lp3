CREATE TABLE
	ciudades(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE
	paises(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE
	personas(
		id serial PRIMARY KEY,
		descripcion varchar(100) UNIQUE,
		apellido varchar(100),
		cedula TEXT NOT NULL	
	); 

CREATE TABLE
	generos(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE
	estado_civiles(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);
 
CREATE TABLE
	ocupaciones(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
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

CREATE TABLE
	enfermedades(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE
	dias(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);	

CREATE TABLE
	horas(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);		

CREATE TABLE
	turnos(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE
	servicios(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE
	tipo_pagos(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE
	departamentos(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

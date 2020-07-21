# -*- coding: utf-8 -*-

import pymongo

import datetime

import csv

import pandas as pd

NOMBRE_BD         = "arbolados_bonaerenses"

NOMBRE_COLLEC     = "barrios_max_cant_arbol_requerido"

MONGO_URI         = "mongodb+srv://stephanie:JOWCqLDG5Bq2DbgI@cluster0-lmmsw.mongodb.net/arbolados_bonaerenses?retryWrites=true&w=majority"

CONN_ATLAS        = "atlas"

client = pymongo.MongoClient(MONGO_URI)
db = client.barrio


from pymongo import MongoClient

#Decidi utilizar el nombre cientifico por que es universal

ARBOL_REQUERIDO   = 'Phytolacca dioica'

NUEVO_CSV         = 'arbolado-publico-lineal-actual.csv'

ARCHIVO_AUX       = 'aux.csv'

NOMBRE_CIENTIFICO = 'nombre_cientifico'

BARRIO_CSV        = 'barrio'

ARCHIVO_CSV       = 'arbolado-publico-lineal.csv'

MONGO_URI         = 'mongodb://localHost'

CONN_ATLAS        = "atlas"

class DB:

	_instance = None
	__conn    = None
	database  = None

	def __new__(cls):

		if cls._instance in None:

			cls._instance = super(DB, cls).__new__(cls)

		return cls._instance

	def __init__(self):

		if self.__conn is None:

			conn_type = CONN_ATLAS

			if conn_type == CONN_ATLAS:

				# Conexión con la DB de Atlas

				self.__conn = pymongo.MongoClient(MONGO_URI)

			else:
				raise ValueError(" Connection error")

			self.database = self.__conn["nombre_base_datos"]

# Test section 

""" 
	Precondición: El archivo con extencion csv debe existir para poder realizar la lectura requerida.
				  La base de datos debe ser limpiada previamente.

	Postcondición: Devuelve un registro en la base de datos de la cantidas de ombues en la ciudad de Bs.As,
				  clasificandolos por barrio, y por pantalla la cantidad de ombues barrialmente ademas de 
				  lo que esto representa porcentualmente en toda la provincia.
				   
"""


def imprimir_datos_actualizados(archivo, total_arboles):

	datos = pd.read_csv(archivo)

	print(dato_arbol)

	ombues = len(archivo.readlines())

	datos.close()

	porcentaje = (ombues*100)/total_arboles

	print("El porcentaje de ombues con respecto al total de arboles des de un ",porcentaje +"% \n")
	print("El total de arboles en la ciudad de Buenos Aires es de ",total_arboles+"\n")


def filtrar_datos(archivo):
	
	contador = 0

	archivo = pd.read_csv(ARCHIVO_CSV, header = 0)

	archivo_temp = open(ARCHIVO_AUX, "w")

	if (archivo):
		
		archivo_temp.write(archivo[NOMBRE_CIENTIFICO,BARRIO_CSV])
	
	archivo_temp.close()
	archivo_temp = open(ARCHIVO_AUX,"r")

	lineas = archivo_temp.read().splitlines()

	for linea in lineas:
		if linea.split(ARBOL_REQUERIDO):
			contador +1
			if linea.split(BARRIO_CSV) < linea.split(BARRIO_CSV-1):
				data_querry = {inea.split(BARRIO_CSV) : contador}

	return data_querry


def escribir_archivo(dictionary):

	csv_nuevo = open(NUEVO_CSV,"w")

	encabezado = FORMATO;

	csv_nuevo.write(encabezado)

	for key in dictionary.keys():
		
		barrio = key

		cantidad = dictionary[key]

		form = barrio + ";" + cantidad + "\n"

		csv_nuevo.write(form)

if __name__ == '__main__':

	for docId in toRemove:
		db.data.remove({"arobolado_bonaerense":docId})
	
	db = DB()

	data = db.database["arobolado_bonaerense"]

	dictionary = filtrar_datos(ARCHIVO_CSV)

	archivo_actualizado =  escribir_archivo(dictionary)

	data_count = data.find(dictionary).count()

	imprimir_datos_actualizados(archivo_actualizado,data_count)
	print("Cantidad (",datetime.datetime.now(), ") :", data_count)

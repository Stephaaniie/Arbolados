# -*- coding: utf-8 -*-

import datetime

import csv

import pymongo

import pandas as pd

from pymongo import MongoClient

REGISTRO_OMBUES_CANT = 'cant_ombues_barrio.csv'

NOMBRE_BD         = "arbolados_bonaerenses"

NOMBRE_COLLEC     = "barrio"

MONGO_URI         = "mongodb+srv://stephanie:stephanie@cluster0-lmmsw.mongodb.net/test?retryWrites=true&w=majority"

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

			self.database = self.__conn[NOMBRE_BD]



# Test section 

if __name__ == '__main__':
	
	db = DB()

	data = db.database[NOMBRE_COLLEC]

	nuevos_datos = pd.read_csv(REGISTRO_OMBUES_CANT)

	data_frame = pd.DataFrame(nuevos_datos)

	barios_cant_max = data_frame.get_value(data_frame['Cantidad de Ombús:'].idxmax(),'barrio')

	print(barios_cant_max)
	
	#grupo = data_frame2.groupby(COLUMNA_REQUERIDA)

	

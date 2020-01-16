# -*- coding: utf-8 -*-

import datetime

import csv

import pandas as pd

import pymongo

from pymongo import MongoClient

#Decidi utilizar el nombre cientifico por que es universal

ARBOL_REQUERIDO   = 'Phytolacca dioica'

NOMBRE_BD         = "arbolados_bonaerenses"

NOMBRE_COLLEC     = "barrio"

NUEVO_CSV         = 'arbolado-publico-lineal-actual.csv'

ARCHIVO_AUX       = 'aux.csv'

NOMBRE_CIENTIFICO = 'nombre_cie'

BARRIO_CSV        = 'barrio'

ARCHIVO_CSV       = 'arbolado-publico-lineal.csv'

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

	db.createCollection(NOMBRE_COLLEC)

	db.barrio.drop()

	data = db.database[NOMBRE_COLLEC]

	data_query = {'campo' : 'valor'}

	"""data_count = data.find(data_query).count()

	print("Cantidad (",datetime.datetime.now(), ") :", data_count)"""

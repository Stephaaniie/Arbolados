# -*- coding: utf-8 -*-

import datetime

import csv

import pymongo

from pymongo import MongoClient

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

	data_query = {'campo' : 'valor'}

	"""data_count = data.find(data_query).count()

	print("Cantidad (",datetime.datetime.now(), ") :", data_count)"""

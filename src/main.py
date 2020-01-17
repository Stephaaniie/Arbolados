# -*- coding: utf-8 -*-

import db_connect

import generador_archivo_info

NOMBRE_BD         = "arbolados_bonaerenses"

NOMBRE_COLLEC     = "barrios_max_cant_arbol_requerido"

ARBOL_REQUERIDO   = 'Ombú'

COLUMNA_REQUERIDA = 'barrio'

NOM_COL_FILTRAR   = "nombre_com"

REGISTRO_BONAERENSE = 'arbolado-publico-lineal.csv'

REGISTRO_OMBUES     = 'ombues_barrio.csv'

REGISTRO_OMBUES_CANT = 'cant_ombues_barrio.csv'

CANTIDAD_MAX         = 9

import pandas as pd

datos = pd.read_csv(REGISTRO_BONAERENSE)

data_frame = pd.DataFrame(datos)

datos.set_index(NOM_COL_FILTRAR,inplace = True)

data_frame = datos.loc[[ARBOL_REQUERIDO],[COLUMNA_REQUERIDA]]

data_frame.reset_index().to_csv(REGISTRO_OMBUES, header = True, index = False)

nuevos_datos = pd.read_csv(REGISTRO_OMBUES)

data_frame2 = pd.DataFrame(nuevos_datos)

s = data_frame2.groupby(data_frame2.columns.tolist(), as_index=False).size()

data_frame3 = s[s > 1].reset_index()

data_frame3.rename(columns={0: "Cantidad de Ombús:"}, inplace=True)

data_frame3.reset_index().to_csv(REGISTRO_OMBUES_CANT, header = True, index = False)

with open(REGISTRO_OMBUES,"rU") as f:
    cantidad_ombues = float(sum(1 for row in f))

with open(REGISTRO_BONAERENSE,"rU") as f:
    cantidad_arboles = float(sum(1 for row in f))

promedio = float((cantidad_ombues/cantidad_arboles)*100)

print(data_frame3)

print('La cantidad total de Ombús en la ciudad de Buenos Aires es de: %i'%cantidad_ombues)

print('La catidad total de arboles en la ciudad de Buenos Aires es de:%i'%cantidad_arboles)

print('El porsentaje que representa es de: %f '%promedio)

db = db_connect.DB()

data = db.database[NOMBRE_COLLEC]

data.drop()

aux = data.insert_many(data_frame3)

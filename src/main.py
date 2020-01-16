# -*- coding: utf-8 -*-

import db_connect

print("imprimir archivos")

#Decidi utilizar el nombre cientifico por que es universal

ARBOL_REQUERIDO   = 'Ombú'

COLUMNA_REQUERIDA = 'barrio'

NOM_COL_FILTRAR   = "nombre_com"

REGISTRO_BONAERENSE = 'arbolado-publico-lineal.csv'

REGISTRO_OMBUES     = 'ombues_barrio.csv'

import pandas as pd

datos = pd.read_csv(REGISTRO_BONAERENSE)

data_frame = pd.DataFrame(datos)

datos.set_index(NOM_COL_FILTRAR,inplace = True)

data_frame = datos.loc[[ARBOL_REQUERIDO],[COLUMNA_REQUERIDA]]

data_frame.reset_index().to_csv(REGISTRO_OMBUES, header = True, index = False)

nuevos_datos = pd.read_csv(REGISTRO_OMBUES)

data_frame2 = pd.DataFrame(nuevos_datos)

grupo = data_frame2.groupby(COLUMNA_REQUERIDA)

# Agrupar por barrio con la cantidad de ombues presentes pero me tiro errores que
# no pude encontrar la solucion en la web.

for name,group in grupo:
   print group


with open(REGISTRO_OMBUES,"rU") as f:
    cantidad_ombues = float(sum(1 for row in f))

with open(REGISTRO_BONAERENSE,"rU") as f:
    cantidad_arboles = float(sum(1 for row in f))

promedio = float((cantidad_ombues/cantidad_arboles)*100)

print('La cantidad total de Ombús en la ciudad de Buenos Aires es de: %i'%cantidad_ombues)
print('La catidad total de arboles en la ciudad de Buenos Aires es de:%i'%cantidad_arboles)
print('El porsentaje que representa es de: %f '%promedio)


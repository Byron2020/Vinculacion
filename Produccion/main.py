import pandas as pd
import numpy as np
import sklearn
from utils import Utils
from models import Models

if __name__=="__main__":
    utils=Utils() #creamos clase
    models=Models()

    data=utils.load_from_excel('./in/DatosJUMAIN.xlsx')
    # Eliminar filas con valores NaN
    data = data.dropna()
    # Convertir columnas categóricas a códigos numéricos
    data['tipo_discapacidad'] = data['tipo_discapacidad'].astype('category').cat.codes
    data['grado_escolar'] = data['grado_escolar'].astype('category').cat.codes
    data['nombre_escuela'] = data['nombre_escuela'].astype('category').cat.codes

    X,y=utils.features_target(data,['grado_escolar', 'tipo_discapacidad', 'nombre_escuela'],['porcentaje_discapacidad'])
    models.grid_training(X,y)
    print(data)
    
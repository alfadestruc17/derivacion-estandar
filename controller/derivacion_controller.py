import numpy as np
import matplotlib.pyplot as plt
from model.derivacion_model import guardar_derivacion, obtener_historial, promedio_derivaciones

def calcular_desviacion(numeros):
    desviacion = np.std(numeros)
    guardar_derivacion(numeros, desviacion)
    return desviacion


import numpy as np
import matplotlib.pyplot as plt
from model.derivacion_model import guardar_derivacion, obtener_historial, promedio_derivaciones

def calcular_desviacion(numeros):
    desviacion = np.std(numeros)
    guardar_derivacion(numeros, desviacion)
    return desviacion

def graficar_derivacion(numeros):
    desviacion = np.std(numeros)
    plt.figure(figsize=(8, 5))
    plt.plot(numeros, marker='o', label='Datos')
    plt.axhline(y=desviacion, color='r', linestyle='--', label=f'Desviación: {desviacion:.2f}')
    plt.title("Gráfico de Desviación Estándar")
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.legend()
    plt.grid(True)
    plt.show()

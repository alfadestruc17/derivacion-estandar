import numpy as np
import matplotlib.pyplot as plt

def ingresar_numeros():
    datos = input("Introduce los números separados por coma (86, 87, 88): ")
    lista_numeros = []
    for x in datos.split(','):
        lista_numeros.append(float(x.strip()))
    return lista_numeros

def calcular_desviacion(nums):
    return np.std(nums)

def mostrar_grafico(nums, desviacion):
    plt.plot(nums, marker='o', label="Datos")
    plt.axhline(y=desviacion, color='r', linestyle='--', label=f"Desviación estándar: {desviacion:.2f}")
    plt.title('Desviación Estándar')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.legend()
    plt.show()

def main():
    print("1. Introducir números manualmente.")
    print("2. Usar datos predefinidos.")
    opcion = input("Elige una opción: ")

    if opcion == '1':
        numeros = ingresar_numeros()
    else:
        numeros = [32, 111, 138, 28, 59, 77, 97]

    desviacion = calcular_desviacion(numeros)
    print("La desviación estándar es:", round(desviacion, 2))
    mostrar_grafico(numeros, desviacion)

if __name__ == '__main__':
    main()
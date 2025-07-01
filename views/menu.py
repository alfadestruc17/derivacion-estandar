from controller.derivacion_controller import calcular_desviacion, graficar_derivacion
from model.derivacion_model import obtener_historial, promedio_derivaciones

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Introducir números manualmente")
    print("2. Usar datos automáticos (speed)")
    print("3. Ver historial de derivaciones")
    print("4. Ver promedio de todas las desviaciones")
    print("5. Graficar última derivación")
    print("6. Salir")
    return input("Seleccione una opción: ")

def ingresar_numeros():
    try:
        cantidad = int(input("¿Cuántos números deseas ingresar?: "))
        numeros = []
        for i in range(cantidad):
            while True:
                try:
                    num = float(input(f"Ingrese número {i + 1}: "))
                    numeros.append(num)
                    break
                except ValueError:
                    print("❌ Entrada inválida. Ingresa un número válido.")
        return numeros
    except ValueError:
        print("❌ Entrada inválida. Por favor ingresa un número entero.")
        return []

def mostrar_historial():
    historial = obtener_historial()
    if historial:
        print("\nHistorial de derivaciones:")
        for id, numeros, desviacion, fecha in historial:
            print(f"{fecha} | Números: [{numeros}] | Desviación: {desviacion:.2f}")
    else:
        print("No hay derivaciones registradas.")

def mostrar_promedio():
    promedio = promedio_derivaciones()
    if promedio is not None:
        print(f"\nPromedio de desviaciones estándar: {promedio:.2f}")
    else:
        print("No hay datos para calcular el promedio.")

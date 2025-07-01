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


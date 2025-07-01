from views.menu import *

def main():
    speed = [86, 87, 88, 86, 87, 85, 86]
    ultima = []

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            numeros = ingresar_numeros()
            if numeros:
                desviacion = calcular_desviacion(numeros)
                print(f"Desviación estándar: {desviacion:.2f}")
                ultima = numeros
        elif opcion == '2':
            desviacion = calcular_desviacion(speed)
            print(f"Desviación estándar: {desviacion:.2f}")
            ultima = speed
        elif opcion == '3':
            mostrar_historial()
        elif opcion == '4':
            mostrar_promedio()
        elif opcion == '5':
            if ultima:
                graficar_derivacion(ultima)
            else:
                print("Aún no se ha realizado una derivación para graficar.")
        elif opcion == '6':
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")

if __name__ == '__main__':
    main()

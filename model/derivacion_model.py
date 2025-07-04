from database.config import get_connection
from datetime import datetime

def guardar_derivacion(numeros, desviacion):
    conn = get_connection()
    cursor = conn.cursor()
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    numeros_str = ','.join(map(str, numeros))
    query = "INSERT INTO derivaciones (numeros, desviacion, fecha) VALUES (%s, %s, %s)"
    cursor.execute(query, (numeros_str, float(desviacion), fecha))
    conn.commit()
    conn.close()

def obtener_historial():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM derivaciones")
    rows = cursor.fetchall()
    conn.close()
    return rows

def promedio_derivaciones():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(desviacion) FROM derivaciones")
    result = cursor.fetchone()[0]
    conn.close()
    return result

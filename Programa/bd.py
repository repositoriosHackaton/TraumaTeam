import mysql.connector

#Conexión a la Base de Datos
config = {
    'user': 'root',
    'password': 'NOcbGRKxrGjJdwrLQIcYrCzDeTezIjFo',
    'host': 'viaduct.proxy.rlwy.net',   
    'database': 'railway',
    'port': '48251',      
    'raise_on_warnings': True
}

# Función para realizar nuestra consulta principal
def traer_medicamentos(id):
    try:
        # Conectar a la base de datos
        conn = mysql.connector.connect(**config)

        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()

        query = "SELECT nombre, descripcion, formula, dosis, receta FROM Medicamentos WHERE id_medicamento = %s"
        params = (id,)

        # Ejecutar una consulta
        cursor.execute(query, params)

        # Obtener el resultado
        resultado = cursor.fetchone()

        if resultado:
            nombre, descripcion, formula, dosis, receta = resultado
            medicamento = {
                'nombre': nombre,
                'descripcion': descripcion,
                'formula': formula,
                'dosis': dosis,
                'receta': receta
            }
            return medicamento
        else:
            print("No se encontró ningún medicamento con ese ID.")
            return None

    except mysql.connector.Error as err:
        print(f"Error al conectar a MySQL: {err}")
        return None

    finally:
        # Cerrar el cursor y la conexión
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

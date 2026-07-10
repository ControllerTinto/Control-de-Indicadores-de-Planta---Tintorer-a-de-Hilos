# 💾 Conexión a base de datos (MariaDB / MySQL vía HeidiSQL)
# 📌 Las credenciales van en variables de entorno (.env), NUNCA en el código.

import os

# pip install mysql-connector-python
# import mysql.connector


def get_connection():
    """
    🔌 Devuelve una conexión a MariaDB.
    Configurar en .env:  DB_HOST, DB_USER, DB_PASS, DB_NAME
    """
    # return mysql.connector.connect(
    #     host=os.getenv("DB_HOST", "localhost"),
    #     user=os.getenv("DB_USER"),
    #     password=os.getenv("DB_PASS"),
    #     database=os.getenv("DB_NAME", "tintoreria"),
    # )
    raise NotImplementedError("Configurar conexión MariaDB con .env")

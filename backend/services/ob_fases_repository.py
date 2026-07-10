from services.oracle_db import get_oracle_connection


def _row_to_dict(cursor, row) -> dict:
    columns = [col[0].lower() for col in cursor.description]
    return dict(zip(columns, row))


def obtener_fase_410_por_ob(numero_ob: str) -> dict | None:
    query = """
        SELECT *
        FROM OB_FASES
        WHERE NUMERO_OB = :numero_ob
          AND CODIGO_FASE = 410
    """

    conn = get_oracle_connection()
    try:
        cursor = conn.cursor()
        try:
            cursor.execute(query, numero_ob=numero_ob)
            row = cursor.fetchone()
            if row is None:
                return None
            return _row_to_dict(cursor, row)
        finally:
            cursor.close()
    finally:
        conn.close()

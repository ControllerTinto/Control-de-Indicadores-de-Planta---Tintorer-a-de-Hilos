# 🧠 Registro de husos activos por OB (NUEVO MÓDULO)

from core.machines import MAQUINAS


# 📦 memoria de husos por OB
husos_por_ob = {}


# 🔧 convierte rango QR a lista
def expandir_rango(rango: str):

    inicio, fin = map(int, rango.split("-"))

    # 🔁 corrige si viene invertido
    if inicio > fin:
        inicio, fin = fin, inicio

    return list(range(inicio, fin + 1))


# 📌 registrar husos activos de una OB
def registrar_husos(ob: str, maquina: str, rangos: list, excluidos: list = []):

    husos = []

    for r in rangos:
        husos.extend(expandir_rango(r))

    # 🧹 eliminar duplicados + defectuosos
    husos = list(set(husos))
    husos = [h for h in husos if h not in excluidos]

    husos.sort()

    husos_por_ob[ob] = {
        "maquina": maquina,
        "husos_activos": husos
    }

    return husos_por_ob[ob]


# 📦 obtener husos de OB
def obtener_husos(ob: str):

    return husos_por_ob.get(ob, None)

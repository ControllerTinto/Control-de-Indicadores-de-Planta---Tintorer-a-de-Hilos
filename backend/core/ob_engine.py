# 🧾 Motor de OBs — registro, unidades generadas y avance
# 📌 Aquí vive el estado de cada OB: proceso, material, máquina,
#    unidades totales, unidades registradas y pasadas.

import math

from core.machines import MAQUINAS
from core.machine_defects_service import listar_defectuosos


OPERACIONES_VALIDAS = {"Bobinado", "Enconado"}

obs_activas: dict[str, dict] = {}


def registrar_ob(ob: str, operacion: str, material: str,
                 maquina: str, tipo_soporte: str,
                 unidades_totales: int) -> dict:

    if operacion not in OPERACIONES_VALIDAS:
        raise ValueError(f"Operación inválida: {operacion}")

    if maquina not in MAQUINAS:
        raise ValueError(f"Máquina no encontrada: {maquina}")

    if unidades_totales <= 0:
        raise ValueError("Las unidades totales deben ser mayores a 0")

    obs_activas[ob] = {
        "ob": ob,
        "operacion": operacion,
        "proceso": operacion,
        "material": material,
        "maquina": maquina,
        "tipo_soporte": tipo_soporte,
        "unidades_totales": unidades_totales,
        "unidades_registradas": 0,
        "tamano_primera_tanda": None,
        "pasadas_requeridas": None,
        "pasada_actual": 0,
        "historial": [],   # 🆕 lista de cantidades registradas, en orden
    }

    return obs_activas[ob]


def registrar_unidades(ob: str, unidades: int) -> dict:

    data = obtener_ob(ob)

    if unidades <= 0:
        raise ValueError("Las unidades deben ser mayores a 0")

    nuevo_total = data["unidades_registradas"] + unidades

    if nuevo_total > data["unidades_totales"]:
        raise ValueError(
            f"Se excede el total de la OB "
            f"({nuevo_total} > {data['unidades_totales']})"
        )

    if data["tamano_primera_tanda"] is None:
        data["tamano_primera_tanda"] = unidades
        data["pasadas_requeridas"] = math.ceil(
            data["unidades_totales"] / unidades
        )

    data["unidades_registradas"] = nuevo_total
    data["historial"].append(unidades)   # 🆕 guarda el movimiento

    data["pasada_actual"] = math.ceil(
        nuevo_total / data["tamano_primera_tanda"]
    )

    return estado_ob(ob)


def deshacer_ultimo(ob: str) -> dict:
    """
    ↩️ Revierte el último registro de unidades de esta OB.
    Si era el único registro, también borra el tamaño de tanda
    y las pasadas requeridas (vuelven a quedar sin definir).
    """

    data = obtener_ob(ob)

    if not data["historial"]:
        raise ValueError("No hay registros para deshacer en esta OB")

    ultima_cantidad = data["historial"].pop()
    data["unidades_registradas"] -= ultima_cantidad

    if not data["historial"]:
        # 🔁 no queda ningún registro → vuelve al estado inicial
        data["tamano_primera_tanda"] = None
        data["pasadas_requeridas"] = None
        data["pasada_actual"] = 0
    else:
        data["pasada_actual"] = math.ceil(
            data["unidades_registradas"] / data["tamano_primera_tanda"]
        )

    return estado_ob(ob)


def estado_ob(ob: str) -> dict:

    data = obtener_ob(ob)
    avance = data["unidades_registradas"] / data["unidades_totales"]

    return {
        **data,
        "avance_pct": round(avance * 100, 1),
        "completada": data["unidades_registradas"] >= data["unidades_totales"],
    }


def obtener_ob(ob: str) -> dict:

    if ob not in obs_activas:
        raise ValueError(f"OB no registrada: {ob}")

    return obs_activas[ob]


def listar_obs() -> list[dict]:
    return [estado_ob(ob) for ob in obs_activas]
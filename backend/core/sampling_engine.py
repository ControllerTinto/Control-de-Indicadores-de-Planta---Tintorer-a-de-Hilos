# 📊 Motor de muestreo — % según criticidad y pasadas
#
# Reglas:
#   🟢 Base: 10% de husos activos
#   🔴 Máquina crítica: 15%
#   🔁 Más de 3 pasadas: 20% + factor por pasada extra
#   📌 Mínimo 3 husos por OB
#
#   ⛔ 1ª pasada = solo validación (no hay muestreo oficial)
#   ✅ Desde 2ª pasada = muestreo oficial
#   ⚠️ Excepción: si la OB tiene 1 sola pasada requerida, sí se muestrea en esa pasada

import math
import random

from core.ob_engine import obtener_ob
from core.husos_engine import calcular_husos_activos
from core.critical_engine import es_critica


FACTOR_PASADA = 0.02  # +2% por pasada extra (ajustable con planta)


def calcular_porcentaje(critica: bool, pasada_actual: int) -> float:
    """🎯 Determina el % de muestreo según la pasada ACTUAL (no el total requerido)."""

    if pasada_actual > 3:
        extra = (pasada_actual - 3) * FACTOR_PASADA
        return 0.20 + extra

    if critica:
        return 0.15

    return 0.10


def calcular_muestra(husos_activos: list[int], porcentaje: float) -> int:
    """📐 Tamaño de muestra: mínimo 3, máximo los disponibles."""

    n = math.ceil(len(husos_activos) * porcentaje)
    n = max(3, n)
    n = min(n, len(husos_activos))

    return n


def generar_muestreo(ob: str, unidades_iteracion: int,
                     registros_mes: list, modo: str = "aleatorio") -> dict:

    data = obtener_ob(ob)

    if data["pasadas_requeridas"] is None:
        raise ValueError(
            "Aún no se registró la primera salida de esta OB. "
            "Registra unidades en Control de operación antes de generar muestreo."
        )

    pasada_actual = data["pasada_actual"]
    pasadas_requeridas = data["pasadas_requeridas"]

    es_ob_de_una_pasada = pasadas_requeridas == 1
    es_primera_pasada = pasada_actual <= 1

    if es_primera_pasada and not es_ob_de_una_pasada:
        return {
            "ob": ob,
            "maquina": data["maquina"],
            "operacion": data["operacion"],
            "pasada_actual": pasada_actual,
            "pasadas_requeridas": pasadas_requeridas,
            "muestreo_oficial": False,
            "mensaje": "Primera pasada: solo validación, no se exige muestreo oficial.",
            "muestras": 0,
            "husos_seleccionados": [],
        }

    activos = calcular_husos_activos(ob, unidades_iteracion)

    if not activos:
        raise ValueError("No hay husos activos para muestrear")

    critica = es_critica(registros_mes)

    pct = calcular_porcentaje(critica, pasada_actual)
    n = calcular_muestra(activos, pct)

    if modo == "secuencial":
        paso = len(activos) / n
        seleccion = sorted({activos[int(i * paso)] for i in range(n)})
    else:
        seleccion = sorted(random.sample(activos, n))

    return {
        "ob": ob,
        "maquina": data["maquina"],
        "operacion": data["operacion"],
        "pasada_actual": pasada_actual,
        "pasadas_requeridas": pasadas_requeridas,
        "muestreo_oficial": True,
        "critica": critica,
        "porcentaje": round(pct * 100, 1),
        "muestras": len(seleccion),
        "husos_seleccionados": seleccion,
    }
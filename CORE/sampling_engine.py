# 🎯 Muestreo estadístico con ajuste por pasadas

import math
import random

from core.husos_registry import obtener_husos
from core.critical_engine import es_critica


# 📊 calcula porcentaje base según criticidad y pasadas
def calcular_porcentaje(critica: bool, pasadas: float) -> float:

    if pasadas >= 3:
        return 0.20  # 📈 alta carga → 20%

    return 0.15 if critica else 0.10  # 🔴 crítico 15% / normal 10%


# 📐 calcula número de muestras
def calcular_muestra(husos_activos: list, critica: bool, pasadas: float) -> dict:

    n_husos = len(husos_activos)

    porcentaje = calcular_porcentaje(critica, pasadas)

    # 📈 factor logarítmico por duración del proceso
    factor = math.log(pasadas + 1)

    # 🧮 fórmula final
    n = math.ceil(n_husos * porcentaje * factor)

    # ⚠️ restricciones industriales
    n = max(3, n)
    n = min(n, n_husos)

    return {
        "muestras":   n,
        "porcentaje": porcentaje,
        "factor":     round(factor, 4),
        "pasadas":    round(pasadas, 2)
    }


# 🎯 selecciona husos aleatorios
def seleccionar_husos(husos_activos: list, n: int) -> list:
    return sorted(random.sample(husos_activos, n))


# 🚀 función principal
def generar_muestreo(ob: str, cantidad_ob: int, registros_mes: list) -> dict:

    data = obtener_husos(ob)

    if not data:
        return {"error": f"OB '{ob}' no registrada"}

    husos   = data["husos_activos"]
    n_husos = len(husos)

    # 📐 pasadas = cantidad total OB / husos activos
    pasadas = cantidad_ob / n_husos if n_husos > 0 else 1

    critica   = es_critica(registros_mes)
    resultado = calcular_muestra(husos, critica, pasadas)
    seleccion = seleccionar_husos(husos, resultado["muestras"])

    return {
        "ob":                  ob,
        "maquina":             data["maquina"],
        "husos_activos":       n_husos,
        "cantidad_ob":         cantidad_ob,
        "pasadas":             resultado["pasadas"],
        "critica":             critica,
        "porcentaje_aplicado": resultado["porcentaje"],
        "factor_pasadas":      resultado["factor"],
        "muestras":            resultado["muestras"],
        "husos_seleccionados": seleccion
    }

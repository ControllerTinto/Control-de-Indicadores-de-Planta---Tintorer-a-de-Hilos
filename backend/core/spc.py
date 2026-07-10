# 📊 CONTROL ESTADÍSTICO DE PROCESO (SPC)

import math


def calcular_varianza(valores: list[float]) -> float:
    """📐 Varianza de una lista de valores"""
    if len(valores) < 2:
        return 0.0
    media = sum(valores) / len(valores)
    return sum((x - media) ** 2 for x in valores) / len(valores)


def evaluar_proceso(varianza: float, tipo_medicion: str = "DENSIDAD") -> str:
    """
    🎯 Clasifica estabilidad por desviación estándar
    DENSIDAD: 🟢 ≤0.02 | 🟡 ≤0.05 | 🔴 >0.05
    DUREZA: umbrales provisionales — ajustar con datos reales
    """
    desviacion = math.sqrt(varianza) if varianza > 0 else 0.0

    if tipo_medicion == "DENSIDAD":
        if desviacion <= 0.02:
            return "VERDE"
        if desviacion <= 0.05:
            return "AMARILLO"
        return "ROJO"

    if tipo_medicion == "DUREZA":
        if desviacion <= 0.25:
            return "VERDE"
        if desviacion <= 0.50:
            return "AMARILLO"
        return "ROJO"

    return "SIN_TIPO"

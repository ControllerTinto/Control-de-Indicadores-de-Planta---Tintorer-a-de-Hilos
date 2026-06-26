# 📊 CONTROL ESTADÍSTICO DE PROCESO (SPC)

import math


def calcular_varianza(valores: list[float]) -> float:
    """
    📐 Calcula la varianza de una lista de valores
    """
    if len(valores) < 2:
        return 0.0

    media = sum(valores) / len(valores)
    return sum((x - media) ** 2 for x in valores) / len(valores)


def evaluar_proceso(varianza: float, tipo_medicion: str = "DENSIDAD") -> str:
    """
    🎯 Clasifica la estabilidad del proceso por desviación estándar

    DENSIDAD (g/cm³):
        🟢 VERDE    → desviación ≤ 0.02  (variación ±2 en segunda decimal)
        🟡 AMARILLO → desviación ≤ 0.05  (variación ±5 en segunda decimal)
        🔴 ROJO     → desviación  > 0.05 (proceso fuera de control)

    DUREZA (PSI):
        📌 umbrales provisionales — ajustar con datos reales de planta
    """

    # 📐 varianza → desviación estándar (misma escala que los datos)
    desviacion = math.sqrt(varianza) if varianza > 0 else 0.0

    if tipo_medicion == "DENSIDAD":
        if desviacion <= 0.02:
            return "VERDE"
        if desviacion <= 0.05:
            return "AMARILLO"
        return "ROJO"

    if tipo_medicion == "DUREZA":
        # 📌 ajustar cuando tengas datos reales de PSI
        if desviacion <= 0.25:
            return "VERDE"
        if desviacion <= 0.50:
            return "AMARILLO"
        return "ROJO"

    return "SIN_TIPO"

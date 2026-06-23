# 📊 CONTROL ESTADÍSTICO DE PROCESO (SPC)

def evaluar_proceso(varianza):
    """
    🎯 Clasifica la estabilidad del proceso según la varianza

    📌 Verde   → proceso estable
    📌 Amarillo→ alerta (variación media)
    📌 Rojo    → fuera de control
    """

    # 🟢 Proceso estable (variación baja)
    if varianza < 0.001:
        return "VERDE"

    # 🟡 Advertencia (variación media)
    if varianza < 0.005:
        return "AMARILLO"

    # 🔴 Fuera de control
    return "ROJO"

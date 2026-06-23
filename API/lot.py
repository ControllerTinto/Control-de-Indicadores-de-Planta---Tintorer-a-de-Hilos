# 🔁 cierre de lote + análisis estadístico

from core.session import lote
from core.statistics import calcular_varianza
from core.spc import evaluar_proceso

def siguiente_lote():

    # 📊 datos de densidad
    densidades = [
        r["valor"]
        for r in lote["registros"]
        if r["tipo_medicion"] == "DENSIDAD"
    ]

    # 📊 datos de dureza
    durezas = [
        r["valor"]
        for r in lote["registros"]
        if r["tipo_medicion"] == "DUREZA"
    ]

    # 📊 promedio de densidad
    promedio = sum(densidades) / len(densidades) if densidades else 0

    # 📊 promedio de duerza
    promedio_dureza = sum(durezas) / len(durezas) if durezas else 0

    # 📊 varianza (densidad y dureza)
    varianza_densidad = calcular_varianza(densidades)
    varianza_dureza = calcular_varianza(durezas)


    # 📊 SPC (control visual)
    estado_densidad = evaluar_proceso(varianza_densidad)
    estado_dureza = evaluar_proceso(varianza_dureza)

    # 🧾 resumen del lote
    resumen = {
        "ob": lote["ob"],
        "maquina": lote["maquina"],
        "material": lote["material"],

        # 📊 densidad
        "promedio_densidad": promedio,
        "varianza_densidad": varianza_densidad,
        "estado_densidad": estado_densidad,

        # 📊 dureza
        "promedio_dureza": promedio_dureza,
        "varianza_dureza": varianza_dureza,
        "estado_dureza": estado_dureza

    }

    # 🔄 reset del sistema (nuevo lote)
    lote["ob"] = None
    lote["proceso"] = None
    lote["material"] = None
    lote["tipo_soporte"] = None
    lote["maquina"] = None
    lote["registros"] = []

    return resumen

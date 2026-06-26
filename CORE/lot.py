# 🔁 cierre de lote + promedio

from core.session import lote
from core.spc import calcular_varianza

def siguiente_lote():

    # 📊 separar registros por tipo
    densidades = [
        r["valor"]
        for r in lote["registros"]
        if r["tipo_medicion"] == "DENSIDAD"
    ]

    durezas = [
        r["valor"]
        for r in lote["registros"]
        if r["tipo_medicion"] == "DUREZA"
    ]

    # 📐 promedios
    promedio_densidad = sum(densidades) / len(densidades) if densidades else None
    promedio_dureza   = sum(durezas)   / len(durezas)    if durezas    else None

    # 📊 varianzas
    varianza_densidad = calcular_varianza(densidades) if densidades else None
    varianza_dureza   = calcular_varianza(durezas)   if durezas    else None

    # 💾 resumen del lote
    resumen = {
        "ob":               lote["ob"],
        "maquina":          lote["maquina"],
        "material":         lote["material"],
        "promedio_densidad": promedio_densidad,
        "varianza_densidad": varianza_densidad,
        "promedio_dureza":   promedio_dureza,
        "varianza_dureza":   varianza_dureza,
    }

    # 🔄 reset total
    lote["ob"]          = None
    lote["proceso"]     = None
    lote["material"]    = None
    lote["tipo_soporte"] = None
    lote["maquina"]     = None
    lote["registros"]   = []

    return resumen

# 🌐 Registro principal del sistema

from datetime import datetime

from core.session import lote
from core.density_engine import calcular_densidad
from core.quality_engine import calcular_estado


def grabar(data):

    # 🧾 registro base
    registro = {
        "ob": lote["ob"],
        "fecha": datetime.now(),

        "maquina": lote["maquina"],
        "huso": data["huso"],

        "proceso": lote["proceso"],
        "material": lote["material"],
        "tipo_soporte": lote["tipo_soporte"]
    }

    # 🟢 PRE-TEÑIDO → DENSIDAD
    if lote["proceso"] == "Pre-Teñido":

        r = calcular_densidad(
            lote["proceso"],
            lote["material"],
            lote["tipo_soporte"],
            data["diametro"],
            data["peso"]
        )

        registro.update({
            **r,
            "valor": r["densidad"],
            "tipo_medicion": "DENSIDAD",
            "unidad": "g/cm3",
            "estado": calcular_estado(lote["material"], lote["proceso"], r["densidad"])
        })
        lote["registros"].append(registro)  
         
        # 🧹 limpiar UI (huso, circunferencia, peso)
        return registro

    # 🔵 TEÑIDO → DUREZA
    registro.update({
        "valor": data["dureza"],
        "tipo_medicion": "DUREZA",
        "unidad": "PSI",
        "estado": calcular_estado(lote["material"], "Teñido", data["dureza"])
    })
    lote["registros"].append(registro)
    
    # 🧹 limpiar UI (huso, dureza)
    return registro

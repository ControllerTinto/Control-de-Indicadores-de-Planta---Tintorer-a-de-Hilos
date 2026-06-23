# 🧠 Cálculo principal de densidad industrial

from core.geometry import volumen_cilindro
from core.material_rules import (
    calcular_vint,
    calcular_vcor,
    obtener_peso_tubo,
    ALTURA
)


def calcular_densidad(proceso, material, tipo, diametro, peso):

    altura = ALTURA[tipo]

    # 📦 volumen exterior (cámara)
    vext = volumen_cilindro(diametro, altura)

    # 📦 volumen interior
    vint = calcular_vint(tipo)

    # ➖ corrección poliéster
    vcor = calcular_vcor(material, proceso, tipo)

    # 📐 volumen final útil
    vf = vext - vint - vcor

    # ⚖️ masa neta
    masa = peso - obtener_peso_tubo(tipo)

    # 📊 densidad final
    densidad = masa / vf if vf > 0 else 0

    return {
        "vext": vext,
        "vint": vint,
        "vcor": vcor,
        "vf": vf,
        "masa": masa,
        "densidad": densidad
    }

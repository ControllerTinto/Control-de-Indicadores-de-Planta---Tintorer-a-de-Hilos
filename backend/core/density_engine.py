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

    vext = volumen_cilindro(diametro, altura)   # 📦 volumen exterior (cámara)
    vint = calcular_vint(tipo)                  # 📦 volumen interior
    vcor = calcular_vcor(material, proceso, tipo)  # ➖ corrección poliéster

    vf = vext - vint - vcor                     # 📐 volumen final útil
    masa = peso - obtener_peso_tubo(tipo)       # ⚖️ masa neta

    densidad = masa / vf if vf > 0 else 0

    return {
        "vext": vext, "vint": vint, "vcor": vcor,
        "vf": vf, "masa": masa, "densidad": densidad
    }

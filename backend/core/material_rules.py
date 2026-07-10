# 🧱 Reglas físicas del sistema

import math

ALTURA = {
    "Permeabilidad Alta": 14.67,
    "Permeabilidad Baja": 14.77,
    "Cartón Bobina": 15.38,
    "Cartón Enconado": 15.70
}

DINT = {
    "Permeabilidad Alta": 6.4,
    "Permeabilidad Baja": 6.4,
    "Cartón Bobina": 6.3,
    "Cartón Enconado": 5.5
}

PESO_TUBO = {
    "Permeabilidad Alta": 126.01,
    "Permeabilidad Baja": 139.58,
    "Cartón Bobina": 54.58,
    "Cartón Enconado": 38.48
}


def calcular_vint(tipo):
    # 📦 volumen interno del soporte
    h = ALTURA[tipo]
    d = DINT[tipo]
    return math.pi * (d ** 2 / 4) * h


def calcular_vcor(material, proceso, tipo):
    # ➖ corrección poliéster
    if material != "Poliester":
        return 0
    if tipo != "Cartón Bobina":
        return 0
    if proceso == "Bobinado":
        return 18.36
    if proceso == "Enconado":
        return 19.119
    return 0


def obtener_peso_tubo(tipo):
    # ⚖️ peso del soporte físico
    return PESO_TUBO[tipo]

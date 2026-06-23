# 🧱 Reglas físicas del sistema

import math

ALTURA = {
    "Permeabilidad Alta": 14.67,
    "Permeabilidad Baja": 14.77,
    "Rodete de Cartón": 15.38,
    "Cono de Cartón": 15.70
}

DINT = {
    "Permeabilidad Alta": 6.4,
    "Permeabilidad Baja": 6.4,
    "Rodete de Cartón": 6.3,
    "Cono de Cartón": 5.5
}

PESO_TUBO = {
    "Permeabilidad Alta": 126.01,
    "Permeabilidad Baja": 139.58,
    "Rodete de Cartón": 54.58,
    "Cono de Cartón": 38.48
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

    if tipo != "Rodete de Cartón":
        return 0

    if proceso == "BOBINAR HILO":
        return 18.36

    if proceso == "ENCONAR HILO":
        return 19.119

    return 0


def obtener_peso_tubo(tipo):
    # ⚖️ peso del soporte físico
    return PESO_TUBO[tipo]

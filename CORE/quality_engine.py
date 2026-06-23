# 🎯 Clasificación de calidad

def calcular_estado(material, proceso, valor):

    if proceso == "BOBINAR HILO":

        if material == "Algodón":
            return "BAJO" if valor < 0.35 else "OPTIMO" if valor <= 0.40 else "ALTO"

        if material == "Nylon":
            return "BAJO" if valor < 0.30 else "OPTIMO" if valor <= 0.40 else "ALTO"

        if material == "Poliester":
            return "BAJO" if valor < 0.35 else "OPTIMO" if valor <= 0.39 else "ALTO"

    if proceso == "ENCONAR HILO":

        if material == "Algodón":
            return "BAJO" if valor < 0.40 else "OPTIMO" if valor <= 0.45 else "ALTO"

        if material == "Nylon":
            return "BAJO" if valor < 0.40 else "OPTIMO" if valor <= 0.50 else "ALTO"

        if material == "Poliester":
            return "BAJO" if valor < 0.40 else "OPTIMO" if valor <= 0.55 else "ALTO"

    return "SIN MATERIAL"

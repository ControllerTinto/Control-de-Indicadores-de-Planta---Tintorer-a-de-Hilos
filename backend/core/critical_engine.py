# 🔴 detección de criticidad mensual

def es_critica(registros_mes: list):

    if not registros_mes:
        return False

    total = len(registros_mes)

    inestables = len([
        r for r in registros_mes
        if r["estado"] in ["ALTO", "BAJO", "ROJO"]
    ])

    return (inestables / total) > 0.5

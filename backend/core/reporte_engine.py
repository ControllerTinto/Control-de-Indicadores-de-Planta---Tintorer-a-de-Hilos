# 📈 Motor de reportes — resumen de OB (promedio, varianza, SPC)

from core.ob_engine import obtener_ob
from core.medicion_engine import obtener_registros
from core.husos_engine import obtener_pendientes
from core.spc import calcular_varianza, evaluar_proceso


def resumen_ob(ob: str) -> dict:
    """
    📊 Resumen de trazabilidad de una OB:
    promedios, varianza, estado SPC y husos medidos/pendientes.
    """

    data = obtener_ob(ob)
    registros = obtener_registros(ob)
    husos = obtener_pendientes(ob)

    densidades = [r["valor"] for r in registros
                  if r["tipo_medicion"] == "DENSIDAD"]
    durezas = [r["valor"] for r in registros
               if r["tipo_medicion"] == "DUREZA"]

    resumen = {
        "ob": ob,
        "maquina": data["maquina"],
        "material": data["material"],
        "proceso": data["proceso"],
        "husos_medidos": husos["medidos"],
        "husos_pendientes": husos["pendientes"],
        "total_mediciones": len(registros),
    }

    if densidades:
        var = calcular_varianza(densidades)
        resumen.update({
            "promedio_densidad": sum(densidades) / len(densidades),
            "varianza_densidad": var,
            "spc_densidad": evaluar_proceso(var, "DENSIDAD"),
        })

    if durezas:
        var = calcular_varianza(durezas)
        resumen.update({
            "promedio_dureza": sum(durezas) / len(durezas),
            "varianza_dureza": var,
            "spc_dureza": evaluar_proceso(var, "DUREZA"),
        })

    return resumen

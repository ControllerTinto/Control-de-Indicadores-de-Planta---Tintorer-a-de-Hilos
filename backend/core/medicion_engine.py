# 🧪 Motor de medición — densidad (Bobinado) / dureza (Enconado)

from datetime import datetime

from core.ob_engine import obtener_ob
from core.husos_engine import marcar_medido, obtener_pendientes
from core.density_engine import calcular_densidad
from core.quality_engine import calcular_estado
from utils.validaciones import validar_positivo, validar_huso


# 📦 memoria de registros por OB (luego se persiste en MySQL)
registros_por_ob: dict[str, list[dict]] = {}


def registrar_medicion(ob: str, huso: int, diametro: float = None,
                       peso: float = None, dureza: float = None) -> dict:
    """
    📌 Registra la medición de un huso y lo marca como medido.
    - Bobinado: requiere diámetro + peso → densidad
    - Enconado: requiere dureza (PSI)
    """

    data = obtener_ob(ob)

    validar_huso(data["maquina"], huso)

    registro = {
        "ob": ob,
        "fecha": datetime.now().isoformat(),
        "maquina": data["maquina"],
        "huso": huso,
        "proceso": data["proceso"],
        "material": data["material"],
        "tipo_soporte": data["tipo_soporte"],
    }

    # 🟢 BOBINADO → DENSIDAD
    if data["proceso"] == "Bobinado":

        validar_positivo(diametro, "diámetro")
        validar_positivo(peso, "peso")

        r = calcular_densidad(
            data["proceso"], data["material"],
            data["tipo_soporte"], diametro, peso
        )

        registro.update({
            **r,
            "valor": r["densidad"],
            "tipo_medicion": "DENSIDAD",
            "unidad": "g/cm3",
            "estado": calcular_estado(
                data["material"], data["proceso"], r["densidad"]),
        })

    # 🔵 ENCONADO → DUREZA
    else:
        validar_positivo(dureza, "dureza")

        registro.update({
            "valor": dureza,
            "tipo_medicion": "DUREZA",
            "unidad": "PSI",
            "estado": calcular_estado(
                data["material"], "Enconado", dureza),
        })

    # 💾 guardar y actualizar pendientes
    registros_por_ob.setdefault(ob, []).append(registro)
    pendientes = marcar_medido(ob, huso)

    return {
        "registro": registro,
        "pendientes": pendientes["pendientes"],
        "medidos": pendientes["medidos"],
    }


def obtener_registros(ob: str) -> list[dict]:
    """📦 Todos los registros de una OB."""
    return registros_por_ob.get(ob, [])

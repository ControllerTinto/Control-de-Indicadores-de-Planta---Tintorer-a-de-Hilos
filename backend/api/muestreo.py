# 🌐 API de muestreo — genera lista de husos a medir

from fastapi import APIRouter, HTTPException
from core.sampling_engine import generar_muestreo
from core.husos_engine import asignar_pendientes, obtener_pendientes
from core.ob_engine import obtener_ob

router = APIRouter()


# 6️⃣ generar muestreo de la iteración
@router.post("/muestreo/generar")
def post_muestreo(data: dict):
    """
    Espera: ob, unidades (de la iteración), historial (registros del mes).
    Bobinado → lista secuencial (cámaras a lo largo del día).
    Enconado → lista aleatoria de pendientes.
    """
    try:
        ob = data["ob"]
        info = obtener_ob(ob)

        modo = "secuencial" if info["operacion"] == "Bobinado" else "aleatorio"

        resultado = generar_muestreo(
            ob=ob,
            unidades_iteracion=data["unidades"],
            registros_mes=data.get("historial", []),
            modo=modo,
        )

        # 📋 los seleccionados quedan como pendientes de medición
        asignar_pendientes(ob, resultado["husos_seleccionados"])

        return resultado

    except (ValueError, KeyError) as e:
        raise HTTPException(status_code=400, detail=str(e))


# 3️⃣ lista de pendientes / medidos por OB
@router.get("/muestreo/pendientes/{ob}")
def get_pendientes(ob: str):
    return {"ob": ob, **obtener_pendientes(ob)}

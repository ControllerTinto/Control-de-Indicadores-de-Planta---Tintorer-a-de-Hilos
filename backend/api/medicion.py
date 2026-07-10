# 🌐 API de medición y reportes

from fastapi import APIRouter, HTTPException
from core.medicion_engine import registrar_medicion, obtener_registros
from core.reporte_engine import resumen_ob

router = APIRouter()


# 4️⃣ registrar medición (densidad o dureza según proceso)
@router.post("/medicion/registrar")
def post_medicion(data: dict):
    """
    Espera: ob, huso.
    Bobinado: + diametro, peso.
    Enconado: + dureza.
    """
    try:
        return registrar_medicion(
            ob=data["ob"],
            huso=data["huso"],
            diametro=data.get("diametro"),
            peso=data.get("peso"),
            dureza=data.get("dureza"),
        )
    except (ValueError, KeyError) as e:
        raise HTTPException(status_code=400, detail=str(e))


# 📦 registros de una OB
@router.get("/medicion/{ob}")
def get_registros(ob: str):
    return {"ob": ob, "registros": obtener_registros(ob)}


# 8️⃣ resumen de trazabilidad (promedio, varianza, SPC)
@router.get("/reporte/{ob}")
def get_reporte(ob: str):
    try:
        return resumen_ob(ob)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

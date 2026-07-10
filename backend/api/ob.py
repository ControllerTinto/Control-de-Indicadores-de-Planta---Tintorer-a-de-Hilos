# ðŸŒ API de OBs â€” alta, unidades y planboard

from fastapi import APIRouter, HTTPException
from core.ob_engine import (
    registrar_ob, registrar_unidades, deshacer_ultimo,
    listar_obs, estado_ob
)
from services.ob_fases_repository import obtener_fase_410_por_ob

router = APIRouter()


@router.post("/ob/registrar")
def post_registrar_ob(data: dict):
    try:
        return registrar_ob(
            ob=data["ob"],
            operacion=data["operacion"],
            material=data["material"],
            maquina=data["maquina"],
            tipo_soporte=data["tipo_soporte"],
            unidades_totales=data["unidades_totales"],
        )
    except (ValueError, KeyError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/ob/unidades")
def post_unidades(data: dict):
    try:
        return registrar_unidades(data["ob"], data["unidades"])
    except (ValueError, KeyError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/ob/deshacer")
def post_deshacer(data: dict):
    try:
        return deshacer_ultimo(data["ob"])
    except (ValueError, KeyError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/ob/{numero_ob}/fase-410")
def get_ob_fase_410(numero_ob: str):
    try:
        fase = obtener_fase_410_por_ob(numero_ob)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Error consultando Oracle: {e}")

    if fase is None:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontro OB_FASES para NUMERO_OB={numero_ob} y CODIGO_FASE=410",
        )

    return {"numero_ob": numero_ob, "codigo_fase": 410, "fase": fase}


@router.get("/ob/{ob}")
def get_ob(ob: str):
    try:
        return estado_ob(ob)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/planboard")
def get_planboard():
    return {"obs": listar_obs()}


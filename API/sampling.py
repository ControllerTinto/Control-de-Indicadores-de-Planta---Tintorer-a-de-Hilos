# 🎯 API muestreo de husos

from fastapi import APIRouter
from core.husos_registry import registrar_husos
from core.sampling_engine import generar_muestreo

router = APIRouter()


# 📦 1. registrar husos de OB
@router.post("/husos/registrar")
def registrar(data: dict):
    return registrar_husos(
        ob=data["ob"],
        maquina=data["maquina"],
        rangos=data["rangos"],
        excluidos=data.get("excluidos", [])
    )


# 📊 2. generar muestreo con pasadas
@router.post("/husos/muestreo")
def muestreo(data: dict):
    return generar_muestreo(
        ob=data["ob"],
        cantidad_ob=data["cantidad_ob"],
        registros_mes=data.get("historial", [])
    )

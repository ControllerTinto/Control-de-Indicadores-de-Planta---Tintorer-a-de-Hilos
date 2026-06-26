# 🔁 API cierre de lote

from fastapi import APIRouter
from core.lot import siguiente_lote

router = APIRouter()


# 🔒 cerrar lote activo
@router.post("/lote/cerrar")
def cerrar_lote():
    return siguiente_lote()

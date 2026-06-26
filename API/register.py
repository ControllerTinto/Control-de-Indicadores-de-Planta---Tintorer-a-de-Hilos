# 📊 API registro de densidad / dureza por huso

from fastapi import APIRouter
from core.register import grabar

router = APIRouter()


# 📝 registrar medición de un huso
@router.post("/registro")
def registrar(data: dict):
    return grabar(data)

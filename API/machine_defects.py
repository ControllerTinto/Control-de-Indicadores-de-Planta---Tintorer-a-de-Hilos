# 🌐 API gestión de husos defectuosos

from fastapi import APIRouter
from core.machine_defects_service import (
    agregar_defectuoso,
    remover_defectuoso,
    listar_defectuosos,
    set_defectuosos
)

router = APIRouter()


# 📦 obtener lista
@router.get("/defectos/{maquina}")
def get_defectos(maquina: str):

    return {
        "maquina": maquina,
        "defectuosos": listar_defectuosos(maquina)
    }


# ➕ agregar huso defectuoso
@router.post("/defectos/add")
def add_defecto(data: dict):

    agregar_defectuoso(data["maquina"], data["huso"])

    return {"status": "ok"}


# ➖ eliminar huso defectuoso
@router.post("/defectos/remove")
def remove_defecto(data: dict):

    remover_defectuoso(data["maquina"], data["huso"])

    return {"status": "ok"}


# 📦 reemplazar lista completa
@router.post("/defectos/set")
def set_defectos(data: dict):

    set_defectuosos(data["maquina"], data["lista"])

    return {"status": "ok"}

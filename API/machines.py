# ⚙️ API consulta de máquinas y capacidad de husos

from fastapi import APIRouter
from core.machines import MAQUINAS, obtener_husos

router = APIRouter()


# 📦 listar todas las máquinas
@router.get("/maquinas")
def get_maquinas():
    return {
        "maquinas": list(MAQUINAS.keys())
    }


# 🔢 consultar husos de una máquina
@router.get("/maquinas/{maquina}/husos")
def get_husos(maquina: str):

    if maquina not in MAQUINAS:
        return {"error": f"Máquina '{maquina}' no encontrada"}

    return {
        "maquina": maquina,
        "total_husos": MAQUINAS[maquina],
        "husos": obtener_husos(maquina)
    }

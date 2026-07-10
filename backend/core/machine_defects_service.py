# 🧠 Gestión dinámica de husos defectuosos

from core.machine_defects import HUSOS_DEFECTUOSOS


def agregar_defectuoso(maquina: str, huso: int):
    # ➕ agregar huso defectuoso
    if huso not in HUSOS_DEFECTUOSOS[maquina]:
        HUSOS_DEFECTUOSOS[maquina].append(huso)


def remover_defectuoso(maquina: str, huso: int):
    # ➖ eliminar huso defectuoso (huso reparado vuelve a estar disponible)
    if huso in HUSOS_DEFECTUOSOS[maquina]:
        HUSOS_DEFECTUOSOS[maquina].remove(huso)


def set_defectuosos(maquina: str, lista: list):
    # 📦 reemplazar lista completa
    HUSOS_DEFECTUOSOS[maquina] = lista


def listar_defectuosos(maquina: str):
    # 📊 consultar estado
    return HUSOS_DEFECTUOSOS.get(maquina, [])

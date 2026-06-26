# 🧠 Gestión dinámica de husos defectuosos

from core.machine_defects import HUSOS_DEFECTUOSOS


# ➕ agregar huso defectuoso
def agregar_defectuoso(maquina: str, huso: int):

    if huso not in HUSOS_DEFECTUOSOS[maquina]:
        HUSOS_DEFECTUOSOS[maquina].append(huso)


# ➖ eliminar huso defectuoso
def remover_defectuoso(maquina: str, huso: int):

    if huso in HUSOS_DEFECTUOSOS[maquina]:
        HUSOS_DEFECTUOSOS[maquina].remove(huso)


# 📦 reemplazar lista completa
def set_defectuosos(maquina: str, lista: list):

    HUSOS_DEFECTUOSOS[maquina] = lista


# 📊 consultar estado
def listar_defectuosos(maquina: str):

    return HUSOS_DEFECTUOSOS.get(maquina, [])

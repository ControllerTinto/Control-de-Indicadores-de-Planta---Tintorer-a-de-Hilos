# ⚙️ Máquinas y capacidad de husos

MAQUINAS: dict[str, int] = {
    "ME-01": 60,
    "ME-02": 36,
    "ME-03": 24,
    "ME-04": 12,
    "MB-01": 70,
    "MB-02": 32,
}


def obtener_husos(maquina: str) -> list[int]:
    # 🔢 lista completa de husos según capacidad de máquina
    return list(range(1, MAQUINAS[maquina] + 1))

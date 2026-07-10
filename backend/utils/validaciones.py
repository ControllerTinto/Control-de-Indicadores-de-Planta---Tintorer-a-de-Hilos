# ✅ Validaciones de entrada

from core.machines import MAQUINAS


def validar_positivo(valor, nombre: str):
    """🚫 No permite valores nulos, cero o negativos."""

    if valor is None:
        raise ValueError(f"Falta el valor de {nombre}")

    if valor <= 0:
        raise ValueError(f"El {nombre} debe ser mayor a 0 (recibido: {valor})")


def validar_huso(maquina: str, huso: int):
    """🚫 El huso debe existir dentro de la capacidad de la máquina."""

    if maquina not in MAQUINAS:
        raise ValueError(f"Máquina no encontrada: {maquina}")

    if not (1 <= huso <= MAQUINAS[maquina]):
        raise ValueError(
            f"Huso {huso} fuera de rango para {maquina} "
            f"(1–{MAQUINAS[maquina]})"
        )

# 🔢 Motor de husos por OB — activos, pendientes y medidos
# 📌 Trazabilidad: Huso x OB x Máquina

from core.machines import MAQUINAS
from core.machine_defects_service import listar_defectuosos
from core.ob_engine import obtener_ob


# 📦 memoria: por OB guardamos husos pendientes y medidos
husos_estado: dict[str, dict] = {}


def calcular_husos_activos(ob: str, unidades_iteracion: int) -> list[int]:
    """
    🎯 Según las unidades registradas en esta iteración,
    determina qué husos están activos (los primeros N útiles).
    Ejemplo: 10 unidades → husos 1..10 (saltando defectuosos).
    """

    data = obtener_ob(ob)
    maquina = data["maquina"]

    defectuosos = set(listar_defectuosos(maquina))
    todos = range(1, MAQUINAS[maquina] + 1)

    utiles = [h for h in todos if h not in defectuosos]

    if unidades_iteracion > len(utiles):
        # 🔁 más unidades que husos → una pasada completa
        unidades_iteracion = len(utiles)

    return utiles[:unidades_iteracion]


def asignar_pendientes(ob: str, husos_seleccionados: list[int]) -> dict:
    """
    📋 Registra la lista de husos que deben medirse en esta pasada
    (viene del motor de muestreo). Inicializa medidos vacío.
    """

    data = obtener_ob(ob)

    if ob not in husos_estado:
        husos_estado[ob] = {"maquina": data["maquina"],
                            "pendientes": [], "medidos": []}

    # ➕ agrega sin duplicar y sin repetir ya medidos
    ya = set(husos_estado[ob]["pendientes"]) | set(husos_estado[ob]["medidos"])
    nuevos = [h for h in husos_seleccionados if h not in ya]

    husos_estado[ob]["pendientes"].extend(nuevos)
    husos_estado[ob]["pendientes"].sort()

    return husos_estado[ob]


def marcar_medido(ob: str, huso: int) -> dict:
    """
    ✅ Al registrar la medición, el huso pasa
    de pendientes → medidos.
    """

    if ob not in husos_estado:
        raise ValueError(f"OB sin husos asignados: {ob}")

    estado = husos_estado[ob]

    if huso in estado["pendientes"]:
        estado["pendientes"].remove(huso)

    if huso not in estado["medidos"]:
        estado["medidos"].append(huso)
        estado["medidos"].sort()

    return estado


def obtener_pendientes(ob: str) -> dict:
    """📦 Lista de pendientes y medidos de una OB."""
    return husos_estado.get(ob, {"pendientes": [], "medidos": []})

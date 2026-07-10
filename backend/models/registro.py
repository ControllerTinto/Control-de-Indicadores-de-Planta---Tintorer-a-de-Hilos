# 📦 Estructura de cada registro por huso

from pydantic import BaseModel
from datetime import datetime


class Registro(BaseModel):
    ob: str
    fecha: datetime
    maquina: str
    huso: int
    proceso: str          # Bobinado / Enconado
    material: str
    tipo_soporte: str

    diametro: float | None = None
    peso: float | None = None
    dureza: float | None = None

    vext: float | None = None
    vint: float | None = None
    vcor: float | None = None
    vf: float | None = None
    masa: float | None = None

    valor: float
    tipo_medicion: str    # DENSIDAD / DUREZA
    unidad: str           # g/cm³ / PSI
    estado: str           # BAJO / OPTIMO / ALTO

# 📦 Define la estructura de cada registro por huso

from pydantic import BaseModel
from datetime import datetime


class Registro(BaseModel):

    ob: str              # 🧾 Lote / Orden de producción
    fecha: datetime      # ⏱️ Fecha y hora automática

    maquina: str        # ⚙️ ME-01 / MB-02
    huso: int           # 🔢 posición del huso

    proceso: str        # 🔄 BOBINAR HILO / ENCONAR HILO
    material: str       # 🧵 Algodón / Nylon / Poliéster
    tipo_soporte: str   # 🧱 Rodete / Cartón

    diametro: float | None   # 📡 lectura cámara (cm)
    peso: float | None       # ⚖️ balanza
    dureza: float | None     # 🧪 PSI (solo teñido)

    vext: float | None  # 📦 volumen exterior
    vint: float | None  # 📦 volumen interior
    vcor: float | None  # ➖ corrección poliéster
    vf: float | None    # 📐 volumen final
    masa: float | None  # ⚖️ masa neta

    valor: float        # 📊 resultado final
    tipo_medicion: str  # 📌 DENSIDAD / DUREZA
    unidad: str         # 📏 g/cm³ / PSI

    estado: str         # 🎯 BAJO / OPTIMO / ALTO

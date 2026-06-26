# 🔁 Estado del lote en memoria (control de operación)

lote = {
    "ob":                None,   # 🧾 lote / orden de producción
    "proceso":           None,   # 🔄 Pre-Teñido / Teñido
    "material":          None,   # 🧵 Algodón / Nylon / Poliéster
    "tipo_soporte":      None,   # 🧱 Permeabilidad Alta / Baja / Cartón Bobina / Enconado
    "maquina":           None,   # ⚙️ ME-01 / MB-01 / etc.
    "husos_seleccionados": [],   # 🔢 husos elegidos por el operador
    "registros":         []      # 📊 registros por huso
}

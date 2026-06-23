# 📘 Control de Indicadores de Planta – Tintorería de Hilos

Sistema backend en **Python + FastAPI** para el registro, cálculo y análisis de indicadores operativos en el proceso de Tintorería de Hilos.

---

## 🎯 Objetivo del sistema

Este proyecto permite registrar mediciones físicas por lote, máquina y huso, con el fin de calcular indicadores clave como:

- 📦 Densidad de bobinas antes del teñido  
- 🧪 Dureza del hilo después del proceso  
- 📊 Promedios y variabilidad por lote  
- 🎯 Estados de calidad (BAJO / ÓPTIMO / ALTO)  
- 📉 Control estadístico del proceso (SPC)  

---

## 🧠 Arquitectura del sistema

```text
backend/
│
├── main.py                      # 🚀 Punto de entrada FastAPI
│
├── models/
│   └── registro.py             # 📦 Estructura del dato (Pydantic)
│
├── core/
│   ├── session.py              # 🔁 Estado del lote activo en memoria
│   ├── machines.py             # ⚙️ Catálogo de máquinas y husos
│   ├── geometry.py             # 📐 Cálculos geométricos (volumen)
│   ├── material_rules.py       # 🧱 Reglas físicas del material
│   ├── density_engine.py       # 🧠 Cálculo de densidad industrial
│   ├── quality_engine.py       # 🎯 Clasificación de calidad
│   └── spc.py                  # 📊 Control estadístico del proceso
│
├── api/
│   ├── register.py             # 📊 Registro de mediciones por huso
│   ├── lot.py                 # 🔁 Cierre de lote + promedios
│   └── machines.py            # ⚙️ Consulta de husos por máquina
│
├── services/
│   └── db.py                  # 💾 Conexión futura a MariaDB / MySQL
│
├── schemas/
│   └── requests.py            # 📥 Estructura de entrada del frontend
│
└── utils/
    └── time.py               # ⏱️ Utilidades de fecha y control horario

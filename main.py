# 🚀 Punto de entrada del sistema - Tintorería de Hilos

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 🌐 APIs del sistema
from api.register import router as register_router
from api.lot import router as lot_router
from api.machines import router as machines_router
from api.sampling import router as sampling_router
from api.machine_defects import router as defects_router


# 🧠 crear aplicación FastAPI
app = FastAPI(
    title="Sistema de Control - Tintorería de Hilos",
    description="API para control de densidad, dureza, husos y muestreo industrial",
    version="1.0.0"
)


# 🌍 configuración CORS (frontend puede conectarse sin problemas)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # luego puedes restringir a dominio real
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 📦 registro de rutas del sistema
app.include_router(register_router, prefix="/api")
app.include_router(lot_router, prefix="/api")
app.include_router(machines_router, prefix="/api")
app.include_router(sampling_router, prefix="/api")
app.include_router(defects_router, prefix="/api")


# 🧪 endpoint de salud del sistema
@app.get("/")
def health_check():
    return {
        "status": "ok",
        "system": "Tintorería de Hilos",
        "message": "API funcionando correctamente"
    }

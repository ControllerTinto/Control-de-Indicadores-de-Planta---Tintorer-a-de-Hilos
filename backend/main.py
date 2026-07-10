# 🚀 Punto de entrada — Tintorería de Hilos (v2: flujo por OB con cámaras)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.ob import router as ob_router
from api.muestreo import router as muestreo_router
from api.medicion import router as medicion_router
from api.defectos import router as defectos_router

app = FastAPI(
    title="Sistema de Control - Tintorería de Hilos",
    description="Control de OBs, husos, densidad/dureza, muestreo y planboard",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔒 restringir al dominio real en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ob_router, prefix="/api")
app.include_router(muestreo_router, prefix="/api")
app.include_router(medicion_router, prefix="/api")
app.include_router(defectos_router, prefix="/api")


@app.get("/")
def health_check():
    return {"status": "ok", "system": "Tintorería de Hilos", "version": "2.0.0"}

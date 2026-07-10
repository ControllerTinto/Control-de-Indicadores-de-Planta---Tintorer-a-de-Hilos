import { useState } from "react";
import { useOperacion, registrarUnidades, deshacerUltimo } from "../hooks/useOperacion";
const HUSOS_POR_MAQUINA = { "ME-01": 60, "ME-02": 36, "ME-03": 24, "ME-04": 12, "MB-01": 70, "MB-02": 32 };
import "./Operacion.css";

function Operacion() {
  const { obs, loading, error, recargar } = useOperacion();
  const [obSeleccionada, setObSeleccionada] = useState(null);
  const [cantidadPorOB, setCantidadPorOB] = useState({});
  const [unidades, setUnidades] = useState("");
  const [guardando, setGuardando] = useState(false);
  const [errorForm, setErrorForm] = useState(null);

  async function handleRegistrar() {
    setGuardando(true);
    setErrorForm(null);
    try {
      await registrarUnidades(obSeleccionada.ob, Number(unidades));
      setCantidadPorOB({ ...cantidadPorOB, [obSeleccionada.ob]: unidades });
      setObSeleccionada(null);
      recargar();
    } catch (err) {
      setErrorForm(err.response?.data?.detail || err.message);
    } finally {
      setGuardando(false);
    }
  }

  if (loading) return <p>Cargando OBs...</p>;
  if (error) return <p>Error al conectar con el backend: {error}</p>;

  return (
    <div className="operacion">
      <h2>Control de operación</h2>

      {obs.length === 0 && <p className="operacion-vacio">No hay OBs activas.</p>}

      {obs.map((ob) => (
        <div key={ob.ob} className="operacion-card">
          <div className="operacion-info">
            <strong>OB {ob.ob}</strong> · {ob.maquina} ({HUSOS_POR_MAQUINA[ob.maquina]}h) · {ob.operacion} · {ob.material}
            <div className="operacion-datos">
              <span>Total: {ob.unidades_totales}</span>
              <span>Procesado: {ob.unidades_registradas}</span>
              <span>Pendiente: {ob.unidades_totales - ob.unidades_registradas}</span>
              <span>Pasada: {ob.pasada_actual}/{ob.pasadas_requeridas}</span>
            </div>
          </div>
          <div className="operacion-acciones">
            <button
              className="btn-registrar-salida"
              disabled={ob.completada}
              onClick={() => {
                const pendiente = ob.unidades_totales - ob.unidades_registradas;
                const habitual = cantidadPorOB[ob.ob] || "";
                const sugerido = habitual && Number(habitual) > pendiente ? pendiente : habitual;
                setObSeleccionada(ob);
                setUnidades(sugerido);
              }}
            >
              {ob.completada ? "Completada" : "Registrar salida"}
            </button>
            {ob.historial?.length > 0 && (
              <button
                className="btn-deshacer"
                title={`Deshacer último registro (${ob.historial[ob.historial.length - 1]} uds)`}
                onClick={async () => {
                  if (confirm(`¿Deshacer el último registro de ${ob.historial[ob.historial.length - 1]} unidades?`)) {
                    await deshacerUltimo(ob.ob);
                    recargar();
                  }
                }}
              >
                ↩
              </button>
            )}
          </div>
        </div>
      ))}

      {obSeleccionada && (
        <div className="modal-bg" onClick={() => setObSeleccionada(null)}>
          <div className="modal" onClick={(e) => e.stopPropagation()}>
            <h3>Registrar salida — OB {obSeleccionada.ob}</h3>
            <p className="modal-sub">
              Pendiente actual: {obSeleccionada.unidades_totales - obSeleccionada.unidades_registradas}
            </p>

            <label>Unidades terminadas en esta tanda</label>
            <input
              type="number"
              value={unidades}
              onChange={(e) => setUnidades(e.target.value)}
              autoFocus
            />

            {errorForm && <p className="modal-error">{errorForm}</p>}

            <div className="modal-actions">
              <button onClick={() => setObSeleccionada(null)}>Cancelar</button>
              <button
                className="btn-primary"
                onClick={handleRegistrar}
                disabled={guardando || !unidades || Number(unidades) <= 0}
              >
                {guardando ? "Guardando..." : "Registrar"}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default Operacion;
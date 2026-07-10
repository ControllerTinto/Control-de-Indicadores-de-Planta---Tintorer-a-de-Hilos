import { useState } from "react";
import { usePlanboard } from "../hooks/usePlanboard";
import { registrarOB } from "../hooks/useRegistrarOB";
import "./Planboard.css";

const MAQUINAS = ["ME-01", "ME-02", "ME-03", "ME-04", "MB-01", "MB-02"];
const HUSOS_POR_MAQUINA = { "ME-01": 60, "ME-02": 36, "ME-03": 24, "ME-04": 12, "MB-01": 70, "MB-02": 32 };
function calcularDisponibles(maquina, obsDeMaquina) {
  const ocupados = obsDeMaquina
    .filter((o) => !o.completada)
    .reduce((sum, o) => sum + (o.tamano_primera_tanda || 0), 0);
  return HUSOS_POR_MAQUINA[maquina] - ocupados;
}
const MATERIALES = ["Algodón", "Nylon", "Poliester"];
const SOPORTES = ["Cartón Bobina", "Cartón Enconado", "Permeabilidad Alta", "Permeabilidad Baja"];

function Planboard() {
  const { obs, loading, error, recargar } = usePlanboard();
  const [modalAbierto, setModalAbierto] = useState(false);
  const [form, setForm] = useState({
    ob: "", operacion: "Bobinado", material: "Poliester",
    maquina: "ME-01", tipo_soporte: "Cartón Bobina", unidades_totales: 100,
  });
  const [guardando, setGuardando] = useState(false);
  const [errorForm, setErrorForm] = useState(null);

  async function handleGuardar() {
    setGuardando(true);
    setErrorForm(null);
    try {
      await registrarOB({ ...form, unidades_totales: Number(form.unidades_totales) });
      setModalAbierto(false);
      recargar();
    } catch (err) {
      setErrorForm(err.response?.data?.detail || err.message);
    } finally {
      setGuardando(false);
    }
  }

  if (loading) return <p>Cargando planboard...</p>;
  if (error) return <p>Error al conectar con el backend: {error}</p>;

  return (
    <div className="planboard">
      <div className="planboard-header">
        <h2>Planboard</h2>
        <button className="btn-add-ob" onClick={() => setModalAbierto(true)}>+ Añadir OB</button>
      </div>

      {MAQUINAS.map((maquina) => {
        const obsDeMaquina = obs.filter((o) => o.maquina === maquina);
        return (
          <div key={maquina} className="planboard-row">
            {(() => {
              const obsDeMaquina = obs.filter((o) => o.maquina === maquina);
              const disponibles = calcularDisponibles(maquina, obsDeMaquina);
              const nivel = disponibles === 0 ? "lleno" : disponibles < HUSOS_POR_MAQUINA[maquina] * 0.2 ? "bajo" : "ok";
              return (
                <div className="planboard-maquina">
                  {maquina}
                  <span className={`chip-disponibles chip-${nivel}`}>{disponibles} libres</span>
                </div>
              );
            })()}
            <div className="planboard-slot">
              {obsDeMaquina.length > 0 ? (
                obsDeMaquina.map((ob) => (
                  <div key={ob.ob} className="planboard-bloque">
                    <strong>OB {ob.ob}</strong> · {ob.operacion} · {ob.material}
                    <div className="planboard-barra-bg">
                      <div className="planboard-barra-fill" style={{ width: `${ob.avance_pct}%` }} />
                    </div>
                    <span className="planboard-pct"> {ob.pasada_actual === 0 ? "Pendiente de primera salida" : `${ob.avance_pct}% · Pasada ${ob.pasada_actual}/${ob.pasadas_requeridas}`}</span>
                    <span className={`planboard-estado ${ob.completada ? "estado-completada" : ob.tienePendientes ? "estado-muestreo" : "estado-proceso"}`}>
                      {ob.completada ? "Completada" : ob.tienePendientes ? "Pendiente de muestreo" : "En proceso"}
                    </span>
                  </div>
                ))
              ) : (
                <span className="planboard-vacio">Sin OB asignada</span>
              )}
            </div>
          </div>
        );
      })}

      {modalAbierto && (
        <div className="modal-bg" onClick={() => setModalAbierto(false)}>
          <div className="modal" onClick={(e) => e.stopPropagation()}>
            <h3>Añadir OB</h3>

            <label>OB (7 dígitos)</label>
            <input
              value={form.ob}
              maxLength={7}
              onChange={(e) => setForm({ ...form, ob: e.target.value.replace(/\D/g, "") })}
            />

            <label>Operación</label>
            <select value={form.operacion} onChange={(e) => setForm({ ...form, operacion: e.target.value })}>
              <option value="Bobinado">Bobinado</option>
              <option value="Enconado">Enconado</option>
            </select>

            <label>Material</label>
            <select value={form.material} onChange={(e) => setForm({ ...form, material: e.target.value })}>
              {MATERIALES.map((m) => <option key={m}>{m}</option>)}
            </select>

            <label>Máquina</label>
            <select value={form.maquina} onChange={(e) => setForm({ ...form, maquina: e.target.value })}>
              {MAQUINAS.map((m) => <option key={m} value={m}>{m} ({HUSOS_POR_MAQUINA[m]} husos)</option>)}
            </select>

            <label>Tipo de soporte</label>
            <select value={form.tipo_soporte} onChange={(e) => setForm({ ...form, tipo_soporte: e.target.value })}>
              {SOPORTES.map((s) => <option key={s}>{s}</option>)}
            </select>

            <label>Unidades totales</label>
            <input
              type="number"
              value={form.unidades_totales}
              onChange={(e) => setForm({ ...form, unidades_totales: e.target.value })}
            />

            {errorForm && <p className="modal-error">{errorForm}</p>}

            <div className="modal-actions">
              <button onClick={() => setModalAbierto(false)}>Cancelar</button>
              <button className="btn-primary" onClick={handleGuardar} disabled={guardando || form.ob.length !== 7}>
                {guardando ? "Guardando..." : "Registrar OB"}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default Planboard;
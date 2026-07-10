import { useState } from "react";
import { useMuestreo, generarMuestreo, registrarMedicion } from "../hooks/useMuestreo";
const HUSOS_POR_MAQUINA = { "ME-01": 60, "ME-02": 36, "ME-03": 24, "ME-04": 12, "MB-01": 70, "MB-02": 32 };
import "./Muestreo.css";

function Muestreo() {
  const { obs, pendientesPorOB, loading, error, recargar } = useMuestreo();
  const [medicionActiva, setMedicionActiva] = useState(null); // { ob, huso }
  const [diametro, setDiametro] = useState("");
  const [peso, setPeso] = useState("");
  const [dureza, setDureza] = useState("");
  const [guardando, setGuardando] = useState(false);
  const [errorForm, setErrorForm] = useState(null);
  const [mensajeGenerar, setMensajeGenerar] = useState({});

  async function handleGenerar(ob) {
    try {
      const res = await generarMuestreo(ob.ob, ob.tamano_primera_tanda);
      setMensajeGenerar({ ...mensajeGenerar, [ob.ob]: res.mensaje || `Generado: ${res.muestras} husos` });
      recargar();
    } catch (err) {
      setMensajeGenerar({ ...mensajeGenerar, [ob.ob]: err.response?.data?.detail || err.message });
    }
  }

  async function handleRegistrarMedicion() {
    setGuardando(true);
    setErrorForm(null);
    try {
      const ob = obs.find((o) => o.ob === medicionActiva.ob);
      const datos = { ob: medicionActiva.ob, huso: medicionActiva.huso };
      if (ob.operacion === "Bobinado") {
        datos.diametro = Number(diametro);
        datos.peso = Number(peso);
      } else {
        datos.dureza = Number(dureza);
      }
      await registrarMedicion(datos);
      setMedicionActiva(null);
      setDiametro(""); setPeso(""); setDureza("");
      recargar();
    } catch (err) {
      setErrorForm(err.response?.data?.detail || err.message);
    } finally {
      setGuardando(false);
    }
  }

  if (loading) return <p>Cargando muestreo...</p>;
  if (error) return <p>Error al conectar con el backend: {error}</p>;

  const obsConAvance = obs.filter((o) => o.tamano_primera_tanda);

  return (
    <div className="muestreo">
      <h2>Muestreo</h2>

      {obsConAvance.length === 0 && <p className="muestreo-vacio">No hay OBs con avance registrado aún.</p>}

      {obsConAvance.map((ob) => {
        const pendientes = pendientesPorOB[ob.ob] || [];
        return (
          <div key={ob.ob} className="muestreo-card">
            <div className="muestreo-header">
              <strong>OB {ob.ob}</strong> · {ob.maquina} ({HUSOS_POR_MAQUINA[ob.maquina]}h) · {ob.operacion} · Pasada {ob.pasada_actual}/{ob.pasadas_requeridas}
              <button className="btn-generar" onClick={() => handleGenerar(ob)}>
                Generar muestreo
              </button>
            </div>

            {mensajeGenerar[ob.ob] && <p className="muestreo-msg">{mensajeGenerar[ob.ob]}</p>}

            {pendientes.length > 0 && (
              <div className="muestreo-pendientes">
                <span className="muestreo-label">Husos pendientes:</span>
                {pendientes.map((huso) => (
                  <button
                    key={huso}
                    className="chip-huso"
                    onClick={() => setMedicionActiva({ ob: ob.ob, huso })}
                  >
                    #{huso}
                  </button>
                ))}
              </div>
            )}
          </div>
        );
      })}

      {medicionActiva && (
        <div className="modal-bg" onClick={() => setMedicionActiva(null)}>
          <div className="modal" onClick={(e) => e.stopPropagation()}>
            <h3>Medición — OB {medicionActiva.ob} · Huso #{medicionActiva.huso}</h3>

            {obs.find((o) => o.ob === medicionActiva.ob)?.operacion === "Bobinado" ? (
              <>
                <label>Diámetro</label>
                <input type="number" value={diametro} onChange={(e) => setDiametro(e.target.value)} autoFocus />
                <label>Peso</label>
                <input type="number" value={peso} onChange={(e) => setPeso(e.target.value)} />
              </>
            ) : (
              <>
                <label>Dureza (PSI)</label>
                <input type="number" value={dureza} onChange={(e) => setDureza(e.target.value)} autoFocus />
              </>
            )}

            {errorForm && <p className="modal-error">{errorForm}</p>}

            <div className="modal-actions">
              <button onClick={() => setMedicionActiva(null)}>Cancelar</button>
              <button className="btn-primary" onClick={handleRegistrarMedicion} disabled={guardando}>
                {guardando ? "Guardando..." : "Registrar medición"}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default Muestreo;
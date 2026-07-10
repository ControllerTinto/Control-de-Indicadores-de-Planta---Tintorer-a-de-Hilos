import { useState, useEffect, useCallback } from "react";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api";

export function useMuestreo() {
  const [obs, setObs] = useState([]);
  const [pendientesPorOB, setPendientesPorOB] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const cargar = useCallback(async () => {
    setLoading(true);
    try {
      const res = await axios.get(`${API_URL}/planboard`);
      const lista = res.data.obs;
      setObs(lista);

      const mapa = {};
      await Promise.all(
        lista.map(async (ob) => {
          const pend = await axios.get(`${API_URL}/muestreo/pendientes/${ob.ob}`);
          mapa[ob.ob] = pend.data.pendientes || [];
        })
      );
      setPendientesPorOB(mapa);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { cargar(); }, [cargar]);

  return { obs, pendientesPorOB, loading, error, recargar: cargar };
}

export async function generarMuestreo(ob, unidades) {
  const res = await axios.post(`${API_URL}/muestreo/generar`, { ob, unidades });
  return res.data;
}

export async function registrarMedicion(datos) {
  const res = await axios.post(`${API_URL}/medicion/registrar`, datos);
  return res.data;
}

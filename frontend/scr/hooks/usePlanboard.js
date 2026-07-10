import { useState, useEffect, useCallback } from "react";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api";

export function usePlanboard() {
  const [obs, setObs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const cargar = useCallback(async () => {
    setLoading(true);
    try {
      const res = await axios.get(`${API_URL}/planboard`);
      const lista = res.data.obs;

      const conEstado = await Promise.all(
        lista.map(async (ob) => {
          try {
            const pend = await axios.get(`${API_URL}/muestreo/pendientes/${ob.ob}`);
            const tienePendientes = pend.data.pendientes?.length > 0;
            return { ...ob, tienePendientes };
          } catch {
            return { ...ob, tienePendientes: false };
          }
        })
      );

      setObs(conEstado);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { cargar(); }, [cargar]);

  return { obs, loading, error, recargar: cargar };
}
import { useState, useEffect, useCallback } from "react";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api";

export function useOperacion() {
  const [obs, setObs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const cargar = useCallback(() => {
    setLoading(true);
    axios.get(`${API_URL}/planboard`)
      .then((res) => setObs(res.data.obs))
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  useEffect(() => { cargar(); }, [cargar]);

  return { obs, loading, error, recargar: cargar };
}

export async function registrarUnidades(ob, unidades) {
  const res = await axios.post(`${API_URL}/ob/unidades`, { ob, unidades });
  return res.data;
}

export async function deshacerUltimo(ob) {
  const res = await axios.post(`${API_URL}/ob/deshacer`, { ob });
  return res.data;
}
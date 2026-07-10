import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api";

export async function registrarOB(datos) {
  const res = await axios.post(`${API_URL}/ob/registrar`, datos);
  return res.data;
}
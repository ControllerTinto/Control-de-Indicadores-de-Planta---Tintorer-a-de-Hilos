import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Home.css';

const acciones = [
  {
    path: '/registrar-husos',
    icon: '📦',
    titulo: 'Registrar Huso por OB',
    descripcion: 'Escanea la OB y define los husos activos por rango.',
  },
  {
    path: '/densidad-dureza',
    icon: '🧪',
    titulo: 'Densidad y Dureza',
    descripcion: 'Registra mediciones por huso según proceso y pasada.',
  },
  {
    path: '/husos-inoperativos',
    icon: '⚠️',
    titulo: 'Husos Inoperativos',
    descripcion: 'Gestiona husos fuera de servicio por máquina.',
  },
];

function Home() {
  const navigate = useNavigate();

  return (
    <div className="home">
      <div className="home-header">
        <h1 className="home-title">Control de Calidad</h1>
        <p className="home-sub">Tintorería de Hilos — Selecciona una acción</p>
      </div>

      <div className="home-grid">
        {acciones.map((a) => (
          <button
            key={a.path}
            className="home-card"
            onClick={() => navigate(a.path)}
          >
            <span className="card-icon">{a.icon}</span>
            <span className="card-titulo">{a.titulo}</span>
            <span className="card-desc">{a.descripcion}</span>
          </button>
        ))}
      </div>
    </div>
  );
}

export default Home;

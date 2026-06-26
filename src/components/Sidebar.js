import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import './Sidebar.css';

const menuItems = [
  { label: 'Registrar Huso por OB', path: '/registrar-husos', icon: '📦' },
  { label: 'Densidad y Dureza',      path: '/densidad-dureza',  icon: '🧪' },
  { label: 'Husos Inoperativos',     path: '/husos-inoperativos', icon: '⚠️' },
];

function Sidebar() {
  const navigate  = useNavigate();
  const location  = useLocation();

  return (
    <aside className="sidebar">

      <div className="sidebar-logo">
        <div className="logo-mark">N</div>
        <div className="logo-text">
          <span className="logo-name">Nettalco</span>
          <span className="logo-sub">Tintorería · Control</span>
        </div>
      </div>

      <nav className="sidebar-nav">
        <p className="nav-label">MENÚ</p>
        {menuItems.map((item) => (
          <button
            key={item.path}
            className={`nav-item ${location.pathname === item.path ? 'active' : ''}`}
            onClick={() => navigate(item.path)}
          >
            <span className="nav-icon">{item.icon}</span>
            <span className="nav-text">{item.label}</span>
          </button>
        ))}
      </nav>

    </aside>
  );
}

export default Sidebar;

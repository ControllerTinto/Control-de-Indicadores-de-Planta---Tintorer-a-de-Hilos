import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Home from './pages/Home';
import RegistrarHusos from './pages/RegistrarHusos';
import DensidadDureza from './pages/DensidadDureza';
import HusosInoperativos from './pages/HusosInoperativos';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app-container">
        <Sidebar />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/registrar-husos" element={<RegistrarHusos />} />
            <Route path="/densidad-dureza" element={<DensidadDureza />} />
            <Route path="/husos-inoperativos" element={<HusosInoperativos />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;

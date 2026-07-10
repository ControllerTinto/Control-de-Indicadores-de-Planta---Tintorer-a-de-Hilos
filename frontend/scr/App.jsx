import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Sidebar from "./components/layout/Sidebar";
import Planboard from "./app/Planboard";
import Operacion from "./app/Operacion";
import Muestreo from "./app/Muestreo";
import Husos from "./app/Husos";
import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <div className="app-shell">
        <Sidebar />
        <main className="content">
          <Routes>
            <Route path="/" element={<Navigate to="/planboard" replace />} />
            <Route path="/planboard" element={<Planboard />} />
            <Route path="/operacion" element={<Operacion />} />
            <Route path="/muestreo" element={<Muestreo />} />
            <Route path="/husos" element={<Husos />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
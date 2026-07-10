import { NavLink } from "react-router-dom";
import { LayoutGrid, ClipboardList, Ruler, Wrench } from "lucide-react";
import "./Sidebar.css";

const items = [
  { to: "/planboard", label: "Planboard", icon: LayoutGrid },
  { to: "/operacion", label: "Control de operación", icon: ClipboardList },
  { to: "/muestreo", label: "Muestreo", icon: Ruler },
  { to: "/husos", label: "Husos inoperativos", icon: Wrench },
];

function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar-title">Tintorería de Hilos</div>
      <nav>
        {items.map(({ to, label, icon: Icon }) => (
          <NavLink
            key={to}
            to={to}
            className={({ isActive }) =>
              "sidebar-link" + (isActive ? " active" : "")
            }
          >
            <Icon size={18} />
            <span>{label}</span>
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}

export default Sidebar;
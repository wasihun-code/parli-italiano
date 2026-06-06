import React from 'react';
import { NavLink } from 'react-router-dom';
import { FiHome, FiBook, FiHeadphones, FiCheckSquare, FiUsers, FiBarChart2, FiSettings, FiTool } from 'react-icons/fi';
import './AdminSidebar.css'; // We'll create simple CSS

const navItems = [
  { path: '/admin', label: 'Dashboard', icon: FiHome, end: true },
  { path: '/admin/curriculum', label: 'Curriculum', icon: FiBook, end: false },
  { path: '/admin/audio', label: 'Audio', icon: FiHeadphones, end: true },
  { path: '/admin/certification', label: 'Certification', icon: FiCheckSquare, end: true },
  { path: '/admin/users', label: 'Users', icon: FiUsers, end: false },
  { path: '/admin/analytics', label: 'Analytics', icon: FiBarChart2, end: true },
  { path: '/admin/factory', label: 'Factory Operations', icon: FiTool, end: true },
];

export const AdminSidebar: React.FC = () => {
  return (
    <aside className="admin-sidebar">
      <div className="admin-sidebar-header">
        <h2>Parla Admin</h2>
      </div>
      <nav className="admin-sidebar-nav">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            end={item.end}
            className={({ isActive }) => `admin-nav-item ${isActive ? 'active' : ''}`}
          >
            <item.icon className="admin-nav-icon" />
            <span>{item.label}</span>
          </NavLink>
        ))}
      </nav>
      <div className="admin-sidebar-footer">
        <NavLink to="/" className="admin-nav-item">
          <FiSettings className="admin-nav-icon" />
          <span>Exit Admin</span>
        </NavLink>
      </div>
    </aside>
  );
};

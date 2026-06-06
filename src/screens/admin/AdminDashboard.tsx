import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { FiBook, FiCheckCircle, FiHeadphones, FiMessageSquare, FiUsers, FiCpu } from 'react-icons/fi';
import './AdminDashboard.css';
import { scenarios } from '../../data/scenarios';

export const AdminDashboard: React.FC = () => {
  const [stats] = useState({
    totalScenarios: scenarios.length,
    certifiedScenarios: 116,
    totalLessons: 696, // Mock: 116 * 6
    totalConversations: 464, // Mock: 116 * 4
    audioCoverage: '100%',
    totalUsers: 1450, // Mock
    factoryVersion: 'V2',
    lastRun: '2026-06-04 15:45:32'
  });

  return (
    <div className="admin-dashboard">
      <h1>Dashboard Overview</h1>
      
      <div className="stats-grid">
        <Link to="/admin/curriculum" className="stat-card">
          <div className="stat-icon"><FiBook /></div>
          <div className="stat-info">
            <h3>Total Scenarios</h3>
            <div className="stat-value">{stats.totalScenarios}</div>
          </div>
        </Link>
        
        <Link to="/admin/certification" className="stat-card">
          <div className="stat-icon success"><FiCheckCircle /></div>
          <div className="stat-info">
            <h3>Certified</h3>
            <div className="stat-value">{stats.certifiedScenarios} / {stats.totalScenarios}</div>
          </div>
        </Link>

        <Link to="/admin/audio" className="stat-card">
          <div className="stat-icon"><FiHeadphones /></div>
          <div className="stat-info">
            <h3>Audio Coverage</h3>
            <div className="stat-value">{stats.audioCoverage}</div>
          </div>
        </Link>

        <div className="stat-card">
          <div className="stat-icon"><FiBook /></div>
          <div className="stat-info">
            <h3>Total Lessons</h3>
            <div className="stat-value">{stats.totalLessons}</div>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon"><FiMessageSquare /></div>
          <div className="stat-info">
            <h3>Conversations</h3>
            <div className="stat-value">{stats.totalConversations}</div>
          </div>
        </div>

        <Link to="/admin/users" className="stat-card">
          <div className="stat-icon"><FiUsers /></div>
          <div className="stat-info">
            <h3>Total Users</h3>
            <div className="stat-value">{stats.totalUsers}</div>
          </div>
        </Link>
      </div>

      <div className="dashboard-row">
        <div className="admin-card factory-status-card">
          <h2 className="admin-card-title">Factory V2 Status</h2>
          <div className="factory-status-details">
            <div className="status-item">
              <span className="status-label">Version</span>
              <span className="status-value"><FiCpu /> {stats.factoryVersion}</span>
            </div>
            <div className="status-item">
              <span className="status-label">Last Global Run</span>
              <span className="status-value">{stats.lastRun}</span>
            </div>
            <div className="status-item">
              <span className="status-label">State</span>
              <span className="status-value success">Operational</span>
            </div>
          </div>
          <div className="card-actions">
            <Link to="/admin/factory" className="admin-button">Manage Factory</Link>
          </div>
        </div>
      </div>
    </div>
  );
};

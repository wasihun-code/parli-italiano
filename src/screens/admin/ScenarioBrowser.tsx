import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { FiSearch, FiFilter, FiCheckCircle } from 'react-icons/fi';
import { scenarios } from '../../data/scenarios';
import './AdminCommon.css';

export const ScenarioBrowser: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [filterCategory, setFilterCategory] = useState('All');

  const categories = ['All', ...Array.from(new Set(scenarios.map(s => s.category)))];

  const filteredScenarios = scenarios.filter(s => {
    const matchesSearch = s.title.toLowerCase().includes(searchTerm.toLowerCase()) || 
                          s.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCategory = filterCategory === 'All' || s.category === filterCategory;
    return matchesSearch && matchesCategory;
  });

  return (
    <div className="admin-card">
      <div className="admin-page-header">
        <h2 className="admin-card-title">Scenario Curriculum</h2>
      </div>

      <div className="admin-toolbar">
        <div className="admin-search-bar">
          <FiSearch className="search-icon" />
          <input 
            type="text" 
            placeholder="Search scenarios..." 
            value={searchTerm}
            onChange={e => setSearchTerm(e.target.value)}
          />
        </div>
        <div className="admin-filter">
          <FiFilter className="filter-icon" />
          <select value={filterCategory} onChange={e => setFilterCategory(e.target.value)}>
            {categories.map(c => (
              <option key={c} value={c}>{c}</option>
            ))}
          </select>
        </div>
      </div>

      <div className="admin-table-container">
        <table className="admin-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Category</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {filteredScenarios.map(scenario => (
              <tr key={scenario.id}>
                <td>{scenario.id}</td>
                <td><strong>{scenario.title}</strong><br/><span className="text-sm text-gray">{scenario.description}</span></td>
                <td><span className="admin-badge category">{scenario.category}</span></td>
                <td>
                  <span className="admin-badge success">
                    <FiCheckCircle style={{marginRight: 4}}/> Certified
                  </span>
                </td>
                <td>
                  <Link to={`/admin/curriculum/${scenario.id}`} className="admin-button-small">
                    Inspect
                  </Link>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

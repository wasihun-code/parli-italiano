import React from 'react';
import { FiActivity } from 'react-icons/fi';
import { Link } from 'react-router-dom';
import './AdminCommon.css';

export const UserManagement: React.FC = () => {
  // Mock data for users
  const mockUsers = [
    { id: '1', email: 'user1@example.com', active: true, streak: 12, completion: '45%' },
    { id: '2', email: 'user2@example.com', active: false, streak: 0, completion: '12%' },
    { id: '3', email: 'user3@example.com', active: true, streak: 5, completion: '89%' },
    { id: '4', email: 'user4@example.com', active: true, streak: 34, completion: '100%' },
  ];

  return (
    <div>
      <div className="admin-page-header">
        <h2 className="admin-card-title" style={{ border: 'none', padding: 0, margin: 0 }}>
          User Management
        </h2>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '20px', marginBottom: '30px' }}>
        <div className="admin-card">
          <div style={{ color: '#64748b', fontSize: '0.875rem', textTransform: 'uppercase', marginBottom: '8px' }}>Total Users</div>
          <div style={{ fontSize: '1.8rem', fontWeight: 'bold', color: '#1e293b' }}>1,450</div>
        </div>
        <div className="admin-card">
          <div style={{ color: '#64748b', fontSize: '0.875rem', textTransform: 'uppercase', marginBottom: '8px' }}>Active Users (30d)</div>
          <div style={{ fontSize: '1.8rem', fontWeight: 'bold', color: '#10b981' }}>892</div>
        </div>
        <div className="admin-card">
          <div style={{ color: '#64748b', fontSize: '0.875rem', textTransform: 'uppercase', marginBottom: '8px' }}>Avg Streak</div>
          <div style={{ fontSize: '1.8rem', fontWeight: 'bold', color: '#f59e0b' }}>4.2 Days</div>
        </div>
        <div className="admin-card">
          <div style={{ color: '#64748b', fontSize: '0.875rem', textTransform: 'uppercase', marginBottom: '8px' }}>Avg Completion</div>
          <div style={{ fontSize: '1.8rem', fontWeight: 'bold', color: '#0ea5e9' }}>23%</div>
        </div>
      </div>

      <div className="admin-card">
        <div className="admin-table-container">
          <table className="admin-table">
            <thead>
              <tr>
                <th>User ID</th>
                <th>Email</th>
                <th>Status</th>
                <th>Streak</th>
                <th>Curriculum Completion</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {mockUsers.map(user => (
                <tr key={user.id}>
                  <td>{user.id}</td>
                  <td>{user.email}</td>
                  <td>
                    {user.active ? 
                      <span className="admin-badge success">Active</span> : 
                      <span className="admin-badge error">Inactive</span>}
                  </td>
                  <td><FiActivity style={{marginRight: 5, color: '#f59e0b'}}/> {user.streak}</td>
                  <td>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                      <div style={{ width: '100px', height: '8px', backgroundColor: '#e2e8f0', borderRadius: '4px', overflow: 'hidden' }}>
                        <div style={{ width: user.completion, height: '100%', backgroundColor: '#0ea5e9' }}></div>
                      </div>
                      <span className="text-sm text-gray">{user.completion}</span>
                    </div>
                  </td>
                  <td>
                    <Link to={`/admin/users/${user.id}`} className="admin-button-small">View Details</Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

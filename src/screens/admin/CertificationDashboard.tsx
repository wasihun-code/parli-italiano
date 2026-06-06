import React, { useState } from 'react';
import { FiCheckCircle, FiXCircle, FiPlay } from 'react-icons/fi';
import './AdminCommon.css';
import { scenarios } from '../../data/scenarios';
import { globalCertification, getScenarioCertification } from '../../data/adminDataLoader';

export const CertificationDashboard: React.FC = () => {
  const [isRunning, setIsRunning] = useState(false);

  const handleGlobalRun = () => {
    setIsRunning(true);
    // In Phase 6 this will trigger a real backend API
    setTimeout(() => setIsRunning(false), 3000);
  };

  const passRate = globalCertification?.pass_rate || '0%';
  const passedCount = globalCertification?.passed_count || 0;
  const totalCount = globalCertification?.total || 0;
  const lastRun = globalCertification?.timestamp ? new Date(globalCertification.timestamp).toLocaleString() : 'Never';

  return (
    <div>
      <div className="admin-page-header">
        <h2 className="admin-card-title" style={{ border: 'none', padding: 0, margin: 0 }}>
          Certification Status
        </h2>
        <div style={{ display: 'flex', gap: '10px' }}>
          <button className="admin-button-small" onClick={handleGlobalRun} disabled={isRunning} style={{ backgroundColor: '#0f172a', color: 'white' }}>
            <FiPlay style={{ marginRight: 6 }} />
            {isRunning ? 'Running...' : 'Certify Entire Project'}
          </button>
        </div>
      </div>

      <div className="admin-card" style={{ marginBottom: '20px' }}>
        <h3>Global Overview</h3>
        <p className="text-sm text-gray">Factory Version: V2 | Last Run: {lastRun}</p>
        <div style={{ display: 'flex', gap: '20px', marginTop: '15px' }}>
          <div style={{ flex: 1, backgroundColor: '#f8fafc', padding: '15px', borderRadius: '6px' }}>
            <div className="text-gray text-sm">Pass Rate</div>
            <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: passRate === '100.00%' ? '#16a34a' : '#ef4444' }}>{passRate}</div>
          </div>
          <div style={{ flex: 1, backgroundColor: '#f8fafc', padding: '15px', borderRadius: '6px' }}>
            <div className="text-gray text-sm">Certified Scenarios</div>
            <div style={{ fontSize: '1.5rem', fontWeight: 'bold' }}>{passedCount} / {totalCount}</div>
          </div>
          <div style={{ flex: 1, backgroundColor: '#f8fafc', padding: '15px', borderRadius: '6px' }}>
            <div className="text-gray text-sm">Target Status</div>
            <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#f59e0b' }}>Gold Standard V1</div>
          </div>
        </div>
      </div>

      <div className="admin-card">
        <h3>Scenario Status</h3>
        <div className="admin-table-container">
          <table className="admin-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Scenario</th>
                <th>Category</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {scenarios.map(s => {
                const certData = getScenarioCertification(s.id);
                const isPass = certData?.overall === 'PASS';
                return (
                  <tr key={s.id}>
                    <td>{s.id}</td>
                    <td>{s.title}</td>
                    <td><span className="admin-badge category">{s.category}</span></td>
                    <td>
                      {certData ? (
                        isPass ? 
                          <span className="admin-badge success"><FiCheckCircle style={{marginRight: 4}}/> PASS</span> :
                          <span className="admin-badge error"><FiXCircle style={{marginRight: 4}}/> FAIL</span>
                      ) : (
                        <span className="admin-badge category">NO DATA</span>
                      )}
                    </td>
                    <td>
                      <button className="admin-button-small" onClick={() => alert('API Trigger mocked for Phase 5.5')}>Run Certify</button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

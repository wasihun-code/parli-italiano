import React from 'react';
import { FiTrendingUp, FiTrendingDown, FiClock, FiTarget } from 'react-icons/fi';
import './AdminCommon.css';

export const AnalyticsDashboard: React.FC = () => {
  return (
    <div>
      <div className="admin-page-header">
        <h2 className="admin-card-title" style={{ border: 'none', padding: 0, margin: 0 }}>
          Global Learning Analytics
        </h2>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', marginBottom: '20px' }}>
        <div className="admin-card">
          <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
            <div style={{ padding: '15px', backgroundColor: '#ecfdf5', color: '#10b981', borderRadius: '50%', fontSize: '1.5rem' }}>
              <FiTarget />
            </div>
            <div>
              <div className="text-gray text-sm text-uppercase">Average Global Accuracy</div>
              <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#1e293b' }}>84.2%</div>
            </div>
          </div>
        </div>
        <div className="admin-card">
          <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
            <div style={{ padding: '15px', backgroundColor: '#eff6ff', color: '#3b82f6', borderRadius: '50%', fontSize: '1.5rem' }}>
              <FiClock />
            </div>
            <div>
              <div className="text-gray text-sm text-uppercase">Avg. Time per Lesson</div>
              <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#1e293b' }}>2m 14s</div>
            </div>
          </div>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
        <div className="admin-card">
          <h3 style={{ marginTop: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
            <FiTrendingUp style={{ color: '#10b981' }} /> Most Completed Scenarios
          </h3>
          <ul style={{ padding: 0, listStyle: 'none', margin: 0 }}>
            <li style={{ padding: '10px 0', borderBottom: '1px solid #f1f5f9', display: 'flex', justifyContent: 'space-between' }}>
              <span>Ordering Pizza</span> <strong>1,204 completions</strong>
            </li>
            <li style={{ padding: '10px 0', borderBottom: '1px solid #f1f5f9', display: 'flex', justifyContent: 'space-between' }}>
              <span>Airport Arrival</span> <strong>958 completions</strong>
            </li>
            <li style={{ padding: '10px 0', borderBottom: '1px solid #f1f5f9', display: 'flex', justifyContent: 'space-between' }}>
              <span>Hotel Check-In</span> <strong>890 completions</strong>
            </li>
          </ul>
        </div>

        <div className="admin-card">
          <h3 style={{ marginTop: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
            <FiTrendingDown style={{ color: '#ef4444' }} /> Least Completed Scenarios
          </h3>
          <ul style={{ padding: 0, listStyle: 'none', margin: 0 }}>
            <li style={{ padding: '10px 0', borderBottom: '1px solid #f1f5f9', display: 'flex', justifyContent: 'space-between' }}>
              <span>Household Repair</span> <strong>12 completions</strong>
            </li>
            <li style={{ padding: '10px 0', borderBottom: '1px solid #f1f5f9', display: 'flex', justifyContent: 'space-between' }}>
              <span>Police Report</span> <strong>15 completions</strong>
            </li>
            <li style={{ padding: '10px 0', borderBottom: '1px solid #f1f5f9', display: 'flex', justifyContent: 'space-between' }}>
              <span>Pharmacy Symptoms</span> <strong>24 completions</strong>
            </li>
          </ul>
        </div>

        <div className="admin-card">
          <h3 style={{ marginTop: 0 }}>Most Failed Lessons</h3>
          <p className="text-sm text-gray">Areas where users struggle the most.</p>
          <ul style={{ padding: 0, listStyle: 'none', margin: 0 }}>
            <li style={{ padding: '10px 0', borderBottom: '1px solid #f1f5f9' }}>
              <strong>Lesson 4: Expressing Urgency</strong> (Household Repair) <br/>
              <span className="text-sm text-gray">42% fail rate</span>
            </li>
            <li style={{ padding: '10px 0', borderBottom: '1px solid #f1f5f9' }}>
              <strong>Lesson 3: Complex Symptoms</strong> (Doctor Appointment) <br/>
              <span className="text-sm text-gray">38% fail rate</span>
            </li>
          </ul>
        </div>

        <div className="admin-card">
          <h3 style={{ marginTop: 0 }}>Most Failed Conversations</h3>
          <p className="text-sm text-gray">Conversations with the highest restart rates.</p>
          <ul style={{ padding: 0, listStyle: 'none', margin: 0 }}>
            <li style={{ padding: '10px 0', borderBottom: '1px solid #f1f5f9' }}>
              <strong>Negotiating Price</strong> (Outdoor Market) <br/>
              <span className="text-sm text-gray">55% drop-off</span>
            </li>
            <li style={{ padding: '10px 0', borderBottom: '1px solid #f1f5f9' }}>
              <strong>Describing the Suspect</strong> (Police Report) <br/>
              <span className="text-sm text-gray">48% drop-off</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

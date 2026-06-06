import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { FiArrowLeft, FiTarget } from 'react-icons/fi';
import './AdminCommon.css';

export const UserDetailView: React.FC = () => {
  const { userId } = useParams<{ userId: string }>();

  return (
    <div>
      <div className="admin-page-header">
        <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
          <Link to="/admin/users" className="admin-button-small">
            <FiArrowLeft />
          </Link>
          <h2 className="admin-card-title" style={{ margin: 0, border: 'none', padding: 0 }}>
            User Profile: {userId}
          </h2>
          <span className="admin-badge success">Active</span>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: '20px' }}>
        <div className="admin-card">
          <h3 style={{ marginTop: 0 }}>Overview</h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '15px', marginTop: '20px' }}>
            <div>
              <div className="text-sm text-gray">Email</div>
              <div style={{ fontWeight: 500 }}>user{userId}@example.com</div>
            </div>
            <div>
              <div className="text-sm text-gray">Joined</div>
              <div style={{ fontWeight: 500 }}>Oct 12, 2025</div>
            </div>
            <div>
              <div className="text-sm text-gray">Current Streak</div>
              <div style={{ fontWeight: 500, color: '#f59e0b', display: 'flex', alignItems: 'center', gap: 5 }}>
                <FiTarget /> 12 Days
              </div>
            </div>
            <div>
              <div className="text-sm text-gray">Overall Accuracy</div>
              <div style={{ fontWeight: 500, color: '#10b981' }}>92.4%</div>
            </div>
          </div>
        </div>

        <div className="admin-card">
          <h3 style={{ marginTop: 0 }}>Learning Progress</h3>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '15px', marginBottom: '20px' }}>
            <div style={{ backgroundColor: '#f8fafc', padding: '15px', borderRadius: '8px', textAlign: 'center' }}>
              <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#0ea5e9' }}>45</div>
              <div className="text-sm text-gray">Mastered Scenarios</div>
            </div>
            <div style={{ backgroundColor: '#f8fafc', padding: '15px', borderRadius: '8px', textAlign: 'center' }}>
              <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#8b5cf6' }}>120</div>
              <div className="text-sm text-gray">Completed Lessons</div>
            </div>
            <div style={{ backgroundColor: '#f8fafc', padding: '15px', borderRadius: '8px', textAlign: 'center' }}>
              <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#ec4899' }}>85</div>
              <div className="text-sm text-gray">Conversations Finished</div>
            </div>
          </div>

          <h4>Recent Activity</h4>
          <ul style={{ paddingLeft: '20px', color: '#334155' }}>
            <li>Completed <strong>Asking for Towels</strong> (Accommodation) - <span className="text-sm text-gray">2 hours ago</span></li>
            <li>Finished Conversation 2 in <strong>Airport Arrival</strong> - <span className="text-sm text-gray">Yesterday</span></li>
            <li>Mastered Vocabulary in <strong>Ordering Pizza</strong> - <span className="text-sm text-gray">3 days ago</span></li>
          </ul>
        </div>
      </div>
    </div>
  );
};

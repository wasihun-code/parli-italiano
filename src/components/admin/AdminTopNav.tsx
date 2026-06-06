import React from 'react';
import { FiUser, FiBell } from 'react-icons/fi';
import './AdminTopNav.css';

export const AdminTopNav: React.FC = () => {
  return (
    <header className="admin-topnav">
      <div className="admin-topnav-left">
        {/* Placeholder for breadcrumbs or page title */}
      </div>
      <div className="admin-topnav-right">
        <button className="icon-button">
          <FiBell />
        </button>
        <div className="admin-user-profile">
          <FiUser className="profile-icon" />
          <span>Admin User</span>
        </div>
      </div>
    </header>
  );
};

import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useFriendStore } from '../store/friendStore';
import { apiClient } from '../lib/apiClient';
import { Screen } from '../components/Screen';
import { PrimaryButton } from '../components/PrimaryButton';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { FaSearch, FaUserPlus, FaCheck, FaTimes, FaUserFriends, FaUserClock } from 'react-icons/fa';

export const FriendsScreen: React.FC = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState<any[]>([]);
  const { 
    friends, 
    friendRequests, 
    fetchFriends, 
    fetchFriendRequests, 
    sendRequest, 
    acceptRequest, 
    declineRequest 
  } = useFriendStore();
  const navigate = useNavigate();

  useEffect(() => {
    fetchFriends();
    fetchFriendRequests();
  }, [fetchFriends, fetchFriendRequests]);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;
    try {
      const results = await apiClient.searchUsers(searchQuery);
      setSearchResults(results);
    } catch (err) {
      console.error('Search failed', err);
    }
  };

  const handleSendRequest = async (userId: string) => {
    try {
      await sendRequest(userId);
      alert('Friend request sent!');
      setSearchResults(results => results.filter(u => u.id !== userId));
    } catch (err: any) {
      alert(err.message);
    }
  };

  return (
    <Screen style={{ backgroundColor: colors.surface }}>
      <header style={{ marginBottom: spacing.xl }}>
        <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: 0 }}>Friends 👥</h1>
        <p style={{ color: colors.textSecondary, fontSize: 18, marginTop: spacing.xxs }}>
          Connect and chat with other learners.
        </p>
      </header>

      <div className="max-w-2xl mx-auto p-0 space-y-8" style={{ paddingBottom: 100 }}>
        {/* Search Section */}
        <section className="coffee-card" style={{ cursor: 'default' }}>
          <h2 style={{ fontSize: 18, marginBottom: spacing.md, display: 'flex', alignItems: 'center', gap: 8 }}>
            <FaSearch color={colors.accent} /> Search Users
          </h2>
          <form onSubmit={handleSearch} style={{ display: 'flex', gap: spacing.sm }}>
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Enter username or email"
              style={{
                flex: 1,
                padding: spacing.md,
                borderRadius: 12,
                border: `2px solid ${colors.border}`,
                fontSize: 16,
                backgroundColor: colors.bg,
                outline: 'none'
              }}
            />
            <PrimaryButton label="Search" onPress={() => handleSearch({ preventDefault: () => {} } as any)} />
          </form>
          {searchResults.length > 0 && (
            <div style={{ marginTop: spacing.lg, display: 'flex', flexDirection: 'column', gap: spacing.sm }}>
              {searchResults.map(user => (
                <div key={user.id} style={{ 
                  display: 'flex', 
                  justifyContent: 'space-between', 
                  alignItems: 'center', 
                  padding: spacing.md, 
                  backgroundColor: '#fff', 
                  borderRadius: 12,
                  border: `1px solid ${colors.border}`
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: spacing.md }}>
                    <div style={{ width: 40, height: 40, borderRadius: 20, backgroundColor: colors.accent, color: '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 'bold' }}>
                      {user.username.charAt(0).toUpperCase()}
                    </div>
                    <span style={{ fontWeight: 'bold' }}>{user.username}</span>
                  </div>
                  <button
                    onClick={() => handleSendRequest(user.id)}
                    style={{ 
                      display: 'flex', 
                      alignItems: 'center', 
                      gap: 4, 
                      color: colors.primary, 
                      background: 'none', 
                      border: 'none', 
                      fontWeight: 'bold', 
                      cursor: 'pointer' 
                    }}
                  >
                    <FaUserPlus /> Add
                  </button>
                </div>
              ))}
            </div>
          )}
        </section>

        {/* Friend Requests */}
        {friendRequests.length > 0 && (
          <section className="coffee-card" style={{ borderColor: colors.accent, background: 'rgba(212, 163, 115, 0.05)', cursor: 'default' }}>
            <h2 style={{ fontSize: 18, marginBottom: spacing.md, display: 'flex', alignItems: 'center', gap: 8 }}>
              <FaUserClock color={colors.accent} /> Pending Requests
            </h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.sm }}>
              {friendRequests.map(request => (
                <div key={request.id} style={{ 
                  display: 'flex', 
                  justifyContent: 'space-between', 
                  alignItems: 'center', 
                  padding: spacing.md, 
                  backgroundColor: '#fff', 
                  borderRadius: 12,
                  border: `1px solid ${colors.accent}44`
                }}>
                  <span style={{ fontWeight: 'bold' }}>{request.from_user.username}</span>
                  <div style={{ display: 'flex', gap: spacing.sm }}>
                    <button
                      onClick={() => acceptRequest(request.id)}
                      style={{ 
                        padding: '6px 12px', 
                        backgroundColor: colors.success, 
                        color: '#fff', 
                        borderRadius: 8, 
                        border: 'none', 
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        gap: 4,
                        fontSize: 14,
                        fontWeight: 'bold'
                      }}
                    >
                      <FaCheck /> Accept
                    </button>
                    <button
                      onClick={() => declineRequest(request.id)}
                      style={{ 
                        padding: '6px 12px', 
                        backgroundColor: '#eee', 
                        color: colors.textPrimary, 
                        borderRadius: 8, 
                        border: 'none', 
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        gap: 4,
                        fontSize: 14,
                        fontWeight: 'bold'
                      }}
                    >
                      <FaTimes /> Decline
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Friends List */}
        <section style={{ marginTop: 24 }}>
          <h2 style={{ fontSize: 18, marginBottom: spacing.md, display: 'flex', alignItems: 'center', gap: 8, color: colors.primary }}>
            <FaUserFriends /> Your Friends
          </h2>
          {friends.length === 0 ? (
            <div className="coffee-card" style={{ textAlign: 'center', color: colors.textSecondary, padding: spacing.xl }}>
              <p>You haven't added any friends yet. Use the search box above to find people!</p>
            </div>
          ) : (
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(240px, 1fr))', gap: spacing.md }}>
              {friends.map(friend => (
                <div
                  key={friend.id}
                  onClick={() => navigate(`/chat/${friend.id}`)}
                  className="coffee-card"
                  style={{
                    padding: spacing.md,
                    flexDirection: 'row',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    cursor: 'pointer'
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: spacing.md }}>
                    <div style={{ position: 'relative' }}>
                      <div style={{ width: 48, height: 48, borderRadius: 24, backgroundColor: 'rgba(78, 52, 46, 0.1)', color: colors.primary, display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 'bold', fontSize: 18 }}>
                        {friend.username.charAt(0).toUpperCase()}
                      </div>
                      <div style={{ 
                        width: 12, 
                        height: 12, 
                        borderRadius: 6, 
                        backgroundColor: friend.is_online ? colors.success : '#ccc', 
                        position: 'absolute', 
                        bottom: 0, 
                        right: 0,
                        border: '2px solid #fff' 
                      }} />
                    </div>
                    <div>
                      <div style={{ fontWeight: 'bold', color: colors.primary }}>{friend.username}</div>
                      <div style={{ fontSize: 12, color: colors.textSecondary }}>{friend.is_online ? 'Online' : 'Offline'}</div>
                    </div>
                  </div>
                  <FaSearch color={colors.border} style={{ opacity: 0.5 }} />
                </div>
              ))}
            </div>
          )}
        </section>
      </div>
    </Screen>
  );
};

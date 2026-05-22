import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useFriendStore } from '../store/friendStore';
import { apiClient } from '../lib/apiClient';
import { Screen } from '../components/Screen';
import { PrimaryButton } from '../components/PrimaryButton';

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
  }, []);

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
    <Screen>
      <header style={{ marginBottom: 24 }}>
        <h2>Friends</h2>
      </header>
      <div className="max-w-2xl mx-auto p-4 space-y-8">
        {/* Search Section */}
        <section>
          <h2 className="text-xl font-bold mb-4">Search Users</h2>
          <form onSubmit={handleSearch} className="flex gap-2">
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Username or email"
              className="flex-1 p-2 border rounded-lg dark:bg-gray-800 dark:border-gray-700"
            />
            <PrimaryButton label="Search" onPress={() => handleSearch({ preventDefault: () => {} } as any)} />
          </form>
          {searchResults.length > 0 && (
            <div className="mt-4 space-y-2">
              {searchResults.map(user => (
                <div key={user.id} className="flex justify-between items-center p-3 bg-white dark:bg-gray-800 rounded-lg shadow-sm">
                  <span>{user.username} ({user.email})</span>
                  <button
                    onClick={() => handleSendRequest(user.id)}
                    className="text-blue-500 hover:text-blue-600 font-medium"
                  >
                    Add Friend
                  </button>
                </div>
              ))}
            </div>
          )}
        </section>

        {/* Friend Requests */}
        {friendRequests.length > 0 && (
          <section>
            <h2 className="text-xl font-bold mb-4">Friend Requests</h2>
            <div className="space-y-2">
              {friendRequests.map(request => (
                <div key={request.id} className="flex justify-between items-center p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg border border-blue-100 dark:border-blue-800">
                  <span>{request.from_user.username}</span>
                  <div className="flex gap-2">
                    <button
                      onClick={() => acceptRequest(request.id)}
                      className="px-3 py-1 bg-green-500 text-white rounded-md text-sm"
                    >
                      Accept
                    </button>
                    <button
                      onClick={() => declineRequest(request.id)}
                      className="px-3 py-1 bg-red-500 text-white rounded-md text-sm"
                    >
                      Decline
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Friends List */}
        <section>
          <h2 className="text-xl font-bold mb-4">Your Friends</h2>
          {friends.length === 0 ? (
            <p className="text-gray-500">You haven't added any friends yet.</p>
          ) : (
            <div className="grid gap-3">
              {friends.map(friend => (
                <div
                  key={friend.id}
                  onClick={() => navigate(`/chat/${friend.id}`)}
                  className="flex justify-between items-center p-4 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 cursor-pointer hover:border-blue-300 dark:hover:border-blue-700 transition-colors"
                >
                  <div className="flex items-center gap-3">
                    <div className={`w-3 h-3 rounded-full ${friend.is_online ? 'bg-green-500' : 'bg-gray-300'}`} />
                    <span className="font-medium">{friend.username}</span>
                  </div>
                  <span className="text-gray-400">
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                    </svg>
                  </span>
                </div>
              ))}
            </div>
          )}
        </section>
      </div>
    </Screen>
  );
};

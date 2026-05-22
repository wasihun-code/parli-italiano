import React, { useState, useEffect, useRef } from 'react';
import { useParams } from 'react-router-dom';
import { useFriendStore } from '../store/friendStore';
import { useAuthStore } from '../store/authStore';
import { Screen } from '../components/Screen';

export const ChatScreen: React.FC = () => {
  const { friendId } = useParams<{ friendId: string }>();
  const [message, setMessage] = useState('');
  const { friends, messages, fetchMessages, sendMessage, fetchFriends } = useFriendStore();
  const currentUser = useAuthStore(state => state.currentUser);
  const scrollRef = useRef<HTMLDivElement>(null);

  const friend = friends.find(f => f.id === friendId);
  const friendMessages = friendId ? messages[friendId] || [] : [];

  useEffect(() => {
    if (!friendId) return;
    
    // Initial fetch
    fetchMessages(friendId);
    if (!friend) fetchFriends();

    // Polling
    const interval = setInterval(() => {
      fetchMessages(friendId);
    }, 3000);

    return () => clearInterval(interval);
  }, [friendId]);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [friendMessages]);

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!message.trim() || !friendId) return;
    
    const content = message;
    setMessage('');
    try {
      await sendMessage(friendId, content);
    } catch (err) {
      console.error('Failed to send message', err);
    }
  };

  if (!friend && !friendMessages.length) {
    return (
      <Screen>
        <div className="flex items-center justify-center h-full">
          <p>Loading friend info...</p>
        </div>
      </Screen>
    );
  }

  return (
    <Screen>
      <header>
        <h2>{friend?.username || 'Chat'}</h2>
      </header>
      <div className="flex flex-col h-[calc(100vh-120px)] max-w-2xl mx-auto border-x dark:border-gray-800">
        {/* Messages area */}
        <div 
          ref={scrollRef}
          className="flex-1 overflow-y-auto p-4 space-y-3"
        >
          {friendMessages.map((msg) => {
            const isMe = msg.sender_id === currentUser?.id;
            return (
              <div 
                key={msg.id} 
                className={`flex ${isMe ? 'justify-end' : 'justify-start'}`}
              >
                <div 
                  className={`max-w-[80%] px-4 py-2 rounded-2xl ${
                    isMe 
                      ? 'bg-blue-600 text-white rounded-tr-none' 
                      : 'bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-gray-100 rounded-tl-none'
                  }`}
                >
                  <p>{msg.content}</p>
                  <span className={`text-[10px] block mt-1 ${isMe ? 'text-blue-100' : 'text-gray-500'}`}>
                    {new Date(msg.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </span>
                </div>
              </div>
            );
          })}
        </div>

        {/* Input area */}
        <form onSubmit={handleSendMessage} className="p-4 bg-white dark:bg-gray-950 border-t dark:border-gray-800 flex gap-2">
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type a message..."
            className="flex-1 p-2 border rounded-full dark:bg-gray-800 dark:border-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button 
            type="submit"
            disabled={!message.trim()}
            className="p-2 bg-blue-600 text-white rounded-full hover:bg-blue-700 disabled:opacity-50"
          >
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
            </svg>
          </button>
        </form>
      </div>
    </Screen>
  );
};

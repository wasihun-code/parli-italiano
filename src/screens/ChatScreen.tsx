import React, { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useFriendStore } from '../store/friendStore';
import { useAuthStore } from '../store/authStore';
import { useSubscriptionStore } from '../store/subscriptionStore';
import { Screen } from '../components/Screen';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { FaPaperPlane, FaLock, FaChevronLeft } from 'react-icons/fa';
import { PrimaryButton } from '../components/PrimaryButton';

export const ChatScreen: React.FC = () => {
  const { friendId } = useParams<{ friendId: string }>();
  const navigate = useNavigate();
  const [message, setMessage] = useState('');
  const { friends, messages, fetchMessages, sendMessage, fetchFriends } = useFriendStore();
  const currentUser = useAuthStore(state => state.currentUser);
  const { plan, isValid } = useSubscriptionStore();
  const isPremium = plan !== 'free' && isValid;
  
  const scrollRef = useRef<HTMLDivElement>(null);

  const friend = friends.find(f => f.id.toString() === friendId);
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
  }, [friendId, fetchMessages, fetchFriends, friend]);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [friendMessages]);

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!message.trim() || !friendId) return;
    
    if (!isPremium) {
      return; // Handled by UI disabling, but safety check
    }

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
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100%' }}>
          <p>Loading friend info...</p>
        </div>
      </Screen>
    );
  }

  return (
    <Screen style={{ backgroundColor: '#fff' }}>
      <div style={{ 
        display: 'flex', 
        flexDirection: 'column', 
        height: 'calc(100dvh - 80px)', 
        maxWidth: 800, 
        margin: '0 auto',
        width: '100%'
      }}>
        {/* Chat Header */}
        <header style={{ 
          padding: spacing.md, 
          borderBottom: `1px solid ${colors.border}`, 
          display: 'flex', 
          alignItems: 'center', 
          gap: spacing.md,
          backgroundColor: '#fff'
        }}>
          <button 
            onClick={() => navigate('/friends')}
            style={{ background: 'none', border: 'none', cursor: 'pointer', padding: 8, display: 'flex', alignItems: 'center' }}
          >
            <FaChevronLeft size={20} color={colors.primary} />
          </button>
          <div style={{ width: 40, height: 40, borderRadius: 20, backgroundColor: 'rgba(78, 52, 46, 0.1)', color: colors.primary, display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 'bold' }}>
            {friend?.username.charAt(0).toUpperCase()}
          </div>
          <div>
            <div style={{ fontWeight: 'bold', color: colors.primary }}>{friend?.username}</div>
            <div style={{ fontSize: 12, color: colors.success }}>{friend?.is_online ? 'Online' : 'Offline'}</div>
          </div>
        </header>

        {/* Premium Banner */}
        {!isPremium && (
          <div style={{ 
            backgroundColor: 'rgba(212, 163, 115, 0.1)', 
            padding: spacing.sm, 
            textAlign: 'center', 
            fontSize: 13, 
            color: colors.primary,
            borderBottom: `1px solid ${colors.accent}44`,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: 8
          }}>
            <FaLock size={12} /> Upgrade to Premium to send messages.
          </div>
        )}

        {/* Messages area */}
        <div 
          ref={scrollRef}
          style={{ 
            flex: 1, 
            overflowY: 'auto', 
            padding: spacing.lg, 
            display: 'flex', 
            flexDirection: 'column', 
            gap: spacing.md,
            backgroundColor: colors.bg
          }}
        >
          {friendMessages.map((msg: any) => {
            const isMe = msg.sender_id === currentUser?.id;
            return (
              <div 
                key={msg.id} 
                style={{ 
                  display: 'flex', 
                  justifyContent: isMe ? 'flex-end' : 'flex-start',
                  width: '100%'
                }}
              >
                <div 
                  style={{ 
                    maxWidth: '80%', 
                    padding: `${spacing.sm}px ${spacing.md}px`, 
                    borderRadius: 18,
                    borderTopRightRadius: isMe ? 4 : 18,
                    borderTopLeftRadius: isMe ? 18 : 4,
                    backgroundColor: isMe ? colors.primary : '#fff',
                    color: isMe ? '#fff' : colors.textPrimary,
                    boxShadow: '0 2px 4px rgba(0,0,0,0.05)',
                    position: 'relative'
                  }}
                >
                  <p style={{ margin: 0, fontSize: 16 }}>{msg.message}</p>
                  <span style={{ 
                    fontSize: 10, 
                    display: 'block', 
                    marginTop: 4, 
                    textAlign: 'right',
                    opacity: 0.7 
                  }}>
                    {new Date(msg.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </span>
                </div>
              </div>
            );
          })}
        </div>

        {/* Input area */}
        <form 
          onSubmit={handleSendMessage} 
          style={{ 
            padding: spacing.md, 
            backgroundColor: '#fff', 
            borderTop: `1px solid ${colors.border}`, 
            display: 'flex', 
            gap: spacing.sm,
            alignItems: 'center'
          }}
        >
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder={isPremium ? "Type a message..." : "Upgrade to chat..."}
            disabled={!isPremium}
            style={{ 
              flex: 1, 
              padding: spacing.md, 
              borderRadius: 24, 
              border: `2px solid ${colors.border}`, 
              outline: 'none',
              fontSize: 16,
              backgroundColor: isPremium ? '#fff' : '#f5f5f5'
            }}
          />
          {isPremium ? (
            <button 
              type="submit"
              disabled={!message.trim()}
              style={{ 
                width: 48, 
                height: 48, 
                borderRadius: 24, 
                backgroundColor: colors.primary, 
                color: '#fff', 
                border: 'none', 
                display: 'flex', 
                alignItems: 'center', 
                justifyContent: 'center',
                cursor: 'pointer',
                opacity: message.trim() ? 1 : 0.5,
                transition: 'transform 0.2s'
              }}
              onMouseEnter={e => e.currentTarget.style.transform = 'scale(1.05)'}
              onMouseLeave={e => e.currentTarget.style.transform = 'scale(1)'}
            >
              <FaPaperPlane />
            </button>
          ) : (
            <PrimaryButton 
              label="Upgrade" 
              onPress={() => navigate('/premium')} 
              variant="accent"
              style={{ padding: '0 16px', height: 48, borderRadius: 24 }}
            />
          )}
        </form>
      </div>
    </Screen>
  );
};

import { create } from 'zustand';
import { apiClient } from '../lib/apiClient';

export type Friend = {
  id: string;
  username: string;
  email: string;
  is_online: boolean;
};

export type FriendRequest = {
  id: number;
  from_user: {
    id: string;
    username: string;
    email: string;
  };
  created_at: string;
};

export type Message = {
  id: number;
  sender_id: string;
  receiver_id: string;
  content: string;
  timestamp: string;
  is_read: boolean;
};

type FriendState = {
  friends: Friend[];
  friendRequests: FriendRequest[];
  messages: Record<string, Message[]>; // friendId -> messages
  loading: boolean;
  error: string | null;
  fetchFriends: () => Promise<void>;
  fetchFriendRequests: () => Promise<void>;
  sendRequest: (userId: string) => Promise<void>;
  acceptRequest: (requestId: number) => Promise<void>;
  declineRequest: (requestId: number) => Promise<void>;
  fetchMessages: (friendId: string) => Promise<void>;
  sendMessage: (friendId: string, content: string) => Promise<void>;
};

export const useFriendStore = create<FriendState>((set, get) => ({
  friends: [],
  friendRequests: [],
  messages: {},
  loading: false,
  error: null,

  fetchFriends: async () => {
    set({ loading: true });
    try {
      const friends = await apiClient.getFriends();
      set({ friends, loading: false });
    } catch (err: any) {
      set({ error: err.message, loading: false });
    }
  },

  fetchFriendRequests: async () => {
    try {
      const requests = await apiClient.getFriendRequests();
      set({ friendRequests: requests });
    } catch (err: any) {
      console.error('Failed to fetch friend requests:', err);
    }
  },

  sendRequest: async (userId: string) => {
    try {
      await apiClient.sendFriendRequest(userId);
    } catch (err: any) {
      set({ error: err.message });
      throw err;
    }
  },

  acceptRequest: async (requestId: number) => {
    try {
      await apiClient.acceptFriendRequest(requestId);
      await get().fetchFriendRequests();
      await get().fetchFriends();
    } catch (err: any) {
      set({ error: err.message });
    }
  },

  declineRequest: async (requestId: number) => {
    try {
      await apiClient.declineFriendRequest(requestId);
      await get().fetchFriendRequests();
    } catch (err: any) {
      set({ error: err.message });
    }
  },

  fetchMessages: async (friendId: string) => {
    try {
      const friendMessages = get().messages[friendId] || [];
      const since = friendMessages.length > 0 ? friendMessages[friendMessages.length - 1].timestamp : undefined;
      const newMessages = await apiClient.getMessages(friendId, since);
      
      if (newMessages.length > 0) {
        set(state => ({
          messages: {
            ...state.messages,
            [friendId]: [...friendMessages, ...newMessages]
          }
        }));

        // Mark as read
        const unreadIds = newMessages
          .filter(m => m.sender_id === friendId && !m.is_read)
          .map(m => m.id);
        if (unreadIds.length > 0) {
          await apiClient.markMessagesRead(unreadIds);
        }
      }
    } catch (err: any) {
      console.error('Failed to fetch messages:', err);
    }
  },

  sendMessage: async (friendId: string, content: string) => {
    try {
      const newMessage = await apiClient.sendMessage(friendId, content);
      set(state => ({
        messages: {
          ...state.messages,
          [friendId]: [...(state.messages[friendId] || []), newMessage]
        }
      }));
    } catch (err: any) {
      set({ error: err.message });
    }
  },
}));

const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';

export type AuthResponse = {
  user: {
    id: string;
    username: string;
    email: string;
    native_language: string;
    total_xp: number;
    streak_days: number;
    subscription_plan: string;
    subscription_valid_until: string;
  };
  tokens: {
    refresh: string;
    access: string;
  };
};

async function request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
  let token = localStorage.getItem('auth_token');
  const headers: any = {
    'Content-Type': 'application/json',
    ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
    ...options.headers,
  };

  let response = await fetch(`${BASE_URL}${endpoint}`, {
    ...options,
    headers,
  });

  // Handle 401 Unauthorized
  if (response.status === 401 && !endpoint.includes('/auth/login/') && !endpoint.includes('/auth/token/refresh/')) {
    const refreshToken = localStorage.getItem('refresh_token');
    if (refreshToken) {
      try {
        const refreshResponse = await fetch(`${BASE_URL}/auth/token/refresh/`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ refresh: refreshToken }),
        });

        if (refreshResponse.ok) {
          const data = await refreshResponse.json();
          localStorage.setItem('auth_token', data.access);
          
          // Retry original request with new token
          headers['Authorization'] = `Bearer ${data.access}`;
          response = await fetch(`${BASE_URL}${endpoint}`, {
            ...options,
            headers,
          });
        } else {
          // Refresh failed, clear tokens and force reload to auth
          localStorage.removeItem('auth_token');
          localStorage.removeItem('refresh_token');
          localStorage.removeItem('parla-italiano-auth'); // Clear authStore persistence
          window.location.href = '/auth';
          return {} as T;
        }
      } catch (err) {
        localStorage.removeItem('auth_token');
        localStorage.removeItem('refresh_token');
        localStorage.removeItem('parla-italiano-auth');
        window.location.href = '/auth';
        return {} as T;
      }
    } else {
      // No refresh token, clear and redirect
      localStorage.removeItem('auth_token');
      localStorage.removeItem('parla-italiano-auth');
      window.location.href = '/auth';
      return {} as T;
    }
  }

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    
    // Flatten DRF field-level errors
    let errorMessage = errorData.detail || errorData.error;
    if (!errorMessage && typeof errorData === 'object') {
      const firstKey = Object.keys(errorData)[0];
      if (firstKey) {
        const val = errorData[firstKey];
        errorMessage = Array.isArray(val) ? val[0] : val;
      }
    }
    
    throw new Error(errorMessage || 'API Request failed');
  }

  if (response.status === 204) {
    return {} as T;
  }

  return response.json();
}

export const apiClient = {
  login: async (email: string, password: string) => {
    const data = await request<AuthResponse>('/auth/login/', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
    localStorage.setItem('auth_token', data.tokens.access);
    localStorage.setItem('refresh_token', data.tokens.refresh);
    return data;
  },

  register: async (data: any) => {
    return request('/auth/register/', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  },

  googleLogin: async (accessToken: string) => {
    const data = await request<AuthResponse>('/auth/google/', {
      method: 'POST',
      body: JSON.stringify({ access_token: accessToken }),
    });
    localStorage.setItem('auth_token', data.tokens.access);
    localStorage.setItem('refresh_token', data.tokens.refresh);
    return data;
  },

  getSubscriptionStatus: async () => {
    return request<{ plan: 'free' | 'premium' | 'premium_plus'; is_valid: boolean }>('/subscription/status/');
  },

  getSubscriptionPlans: async () => {
    return request<any[]>('/subscription/plans/');
  },

  createCheckoutSession: async (priceId: string) => {
    return request<{ url: string }>('/subscription/create-checkout/', {
      method: 'POST',
      body: JSON.stringify({ price_id: priceId }),
    });
  },

  batchSync: async (data: any, language: string) => {
    return request('/sync/', {
      method: 'POST',
      body: JSON.stringify({ data, language }),
    });
  },

  recordActivity: async () => {
    return request<{
      streak_days: number;
      last_activity_date: string;
      streak_freezes_used: number;
      streak_freeze_limit: number;
    }>('/users/me/activity/', {
      method: 'POST',
    });
  },

  searchUsers: async (q: string) => {
    return request<any[]>(`/users/search/?q=${encodeURIComponent(q)}`);
  },

  getLeaderboard: async () => {
    return request<any[]>('/leaderboard/');
  },

  sendFriendRequest: async (userId: string) => {
    return request('/friends/request/', {
      method: 'POST',
      body: JSON.stringify({ to_user_id: userId }),
    });
  },

  acceptFriendRequest: async (requestId: number) => {
    return request(`/friends/request/${requestId}/accept/`, {
      method: 'POST',
    });
  },

  declineFriendRequest: async (requestId: number) => {
    return request(`/friends/request/${requestId}/decline/`, {
      method: 'POST',
    });
  },

  getFriendRequests: async () => {
    return request<any[]>('/friends/requests/');
  },

  getFriends: async () => {
    return request<any[]>('/friends/list/');
  },

  sendMessage: async (receiverId: string, message: string) => {
    return request<any>('/chat/messages/', {
      method: 'POST',
      body: JSON.stringify({ receiver_id: receiverId, content: message }),
    });
  },

  getMessages: async (friendId: string, since?: string) => {
    const url = `/chat/messages/?friend_id=${friendId}${since ? `&since=${since}` : ''}`;
    return request<any[]>(url);
  },

  markMessagesRead: async (messageIds: number[]) => {
    return request('/chat/messages/mark_read/', {
      method: 'POST',
      body: JSON.stringify({ message_ids: messageIds }),
    });
  },
};

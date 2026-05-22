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
  const token = localStorage.getItem('auth_token');
  const headers = {
    'Content-Type': 'application/json',
    ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
    ...options.headers,
  };

  const response = await fetch(`${BASE_URL}${endpoint}`, {
    ...options,
    headers,
  });

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
};

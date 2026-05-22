import React, { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { PrimaryButton } from '../components/PrimaryButton';
import { apiClient } from '../lib/apiClient';
import { useSubscriptionStore } from '../store/subscriptionStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

interface Plan {
  id: string;
  name: string;
  price: string;
  price_id: string;
  features: string[];
}

export const PremiumScreen: React.FC = () => {
  const [plans, setPlans] = useState<Plan[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [searchParams] = useSearchParams();
  const { fetchStatus, plan: currentPlan } = useSubscriptionStore();
  const [message, setMessage] = useState<string | null>(null);

  useEffect(() => {
    const loadPlans = async () => {
      try {
        const data = await apiClient.getSubscriptionPlans();
        setPlans(data);
      } catch (err: any) {
        setError(err.message);
      } finally {
        setIsLoading(false);
      }
    };

    loadPlans();

    if (searchParams.get('success') === 'true') {
      setMessage('Subscription successful! Welcome to Premium.');
      fetchStatus();
    }
  }, [searchParams, fetchStatus]);

  const handleSubscribe = async (priceId: string) => {
    try {
      const { url } = await apiClient.createCheckoutSession(priceId);
      window.location.href = url;
    } catch (err: any) {
      alert('Failed to start checkout: ' + err.message);
    }
  };

  return (
    <Screen>
      <div style={{ padding: spacing.xl, maxWidth: 800, margin: '0 auto' }}>
        <h1 style={{ textAlign: 'center', color: colors.primary, marginBottom: spacing.xl }}>
          Upgrade to Premium
        </h1>

        {message && (
          <div style={{ 
            padding: spacing.md, 
            backgroundColor: colors.success + '20', 
            color: colors.success, 
            borderRadius: 12, 
            marginBottom: spacing.xl,
            textAlign: 'center',
            fontWeight: 'bold'
          }}>
            {message}
          </div>
        )}

        {error && (
          <div style={{ color: colors.error, textAlign: 'center', marginBottom: spacing.xl }}>
            {error}
          </div>
        )}

        {isLoading ? (
          <div style={{ textAlign: 'center' }}>Loading plans...</div>
        ) : (
          <div style={{ 
            display: 'grid', 
            gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', 
            gap: spacing.xl 
          }}>
            {Array.isArray(plans) && plans.map((plan) => (
              <div key={plan.id} className="card" style={{ 
                padding: spacing.xl, 
                display: 'flex', 
                flexDirection: 'column',
                border: currentPlan === plan.id.toLowerCase() ? `2px solid ${colors.accent}` : 'none'
              }}>
                <h2 style={{ color: colors.primary, marginBottom: spacing.sm }}>{plan.name}</h2>
                <div style={{ fontSize: 24, fontWeight: 900, marginBottom: spacing.lg }}>
                  {plan.price}
                </div>
                <ul style={{ 
                  flex: 1, 
                  listStyle: 'none', 
                  padding: 0, 
                  marginBottom: spacing.xl,
                  display: 'flex',
                  flexDirection: 'column',
                  gap: spacing.sm
                }}>
                  {plan.features?.map((feature, i) => (
                    <li key={i} style={{ display: 'flex', gap: spacing.sm }}>
                      <span>✅</span>
                      <span>{feature}</span>
                    </li>
                  ))}
                </ul>
                <PrimaryButton 
                  label={currentPlan === plan.id.toLowerCase() ? 'Current Plan' : 'Subscribe'} 
                  onPress={() => handleSubscribe(plan.price_id)}
                  disabled={currentPlan === plan.id.toLowerCase()}
                  variant={plan.name.includes('Plus') ? 'accent' : 'primary'}
                />
              </div>
            ))}
          </div>
        )}
      </div>
    </Screen>
  );
};

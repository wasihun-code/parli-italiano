import React, { useState, useEffect, useRef, useMemo } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { scenarios, ScriptedChoice } from '@shared/data/scenarios';
import { Screen } from '../components/Screen';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { PrimaryButton } from '../components/PrimaryButton';
import { Tts } from '../lib/tts';
import { FeedbackMessage } from '../components/FeedbackMessage';

type ChatMessage = {
  role: 'host' | 'user';
  text: string;
  english?: string;
  id: string;
};

// Fisher-Yates shuffle
function shuffle<T>(array: T[]): T[] {
  const result = [...array];
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
}

export const ScriptedConversationScreen: React.FC = () => {
  const { scenarioId, conversationId } = useParams<{ scenarioId: string; conversationId: string }>();
  const navigate = useNavigate();
  
  const scenario = scenarios.find(s => s.id === Number(scenarioId));
  const conversation = scenario?.scriptedConversations?.find(c => c.id === conversationId);
  
  const [chatHistory, setChatHistory] = useState<ChatMessage[]>([]);
  const [currentMessageId, setCurrentMessageId] = useState<string | null>(null);
  const [selectedChoice, setSelectedChoice] = useState<ScriptedChoice | null>(null);
  const [isCorrect, setIsCorrect] = useState<boolean | null>(null);
  const [showTranslation, setShowTranslation] = useState<boolean>(false);
  const [revealedMessages, setRevealedMessages] = useState<Set<string>>(new Set());
  
  const scrollRef = useRef<HTMLDivElement>(null);

  const currentMessage = conversation?.messages.find(m => m.id === currentMessageId);

  // Randomize choices whenever the current message changes
  const randomizedChoices = useMemo(() => {
    if (!currentMessage?.choices) return [];
    return shuffle(currentMessage.choices);
  }, [currentMessage?.id]);

  const isLatestMessageRevealed = useMemo(() => {
    if (chatHistory.length === 0) return true;
    const lastMsg = chatHistory[chatHistory.length - 1];
    if (lastMsg.role === 'user') return true;
    return revealedMessages.has(lastMsg.id + (chatHistory.length - 1));
  }, [chatHistory, revealedMessages]);

  // Initialize conversation
  useEffect(() => {
    if (conversation && chatHistory.length === 0) {
      const firstMsg = conversation.messages[0];
      setChatHistory([{ role: firstMsg.role, text: firstMsg.text, english: (firstMsg as any).english, id: firstMsg.id }]);
      setCurrentMessageId(firstMsg.id);
      void Tts.speak(firstMsg.text);
    }
  }, [conversation]);

  // Scroll to bottom
  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [chatHistory, currentMessage, isCorrect, showTranslation, revealedMessages]);

  const handleChoice = (choice: ScriptedChoice) => {
    if (isCorrect === true) return; // Prevent double taps after success
    
    setSelectedChoice(choice);

    if (choice.isCorrect) {
      setIsCorrect(true);
    } else {
      setIsCorrect(false);
    }
  };

  const handleContinue = () => {
    if (!selectedChoice || !selectedChoice.isCorrect || !conversation) return;

    const userMessage: ChatMessage = { 
      role: 'user', 
      text: selectedChoice.text, 
      id: `u-${Date.now()}` 
    };

    const nextId = selectedChoice.nextMessageId;
    
    // Diagnostic info
    console.log(`[CONV DIAGNOSTIC] currentNodeId: ${currentMessageId}`);
    console.log(`[CONV DIAGNOSTIC] historyLength: ${chatHistory.length}`);

    if (nextId === 'END') {
      setChatHistory(prev => [...prev, userMessage]);
      setTimeout(() => {
        navigate(`/scenarios/${scenarioId}/lesson/l1/complete`, { replace: true });
      }, 500);
      return;
    }

    if (nextId === 'RESTART') {
        setChatHistory([]);
        setCurrentMessageId(null);
        setSelectedChoice(null);
        setIsCorrect(null);
        setRevealedMessages(new Set());
        return;
    }

    // Find next message: Use explicit ID or sequential fallback
    let nextMsg: any = null;
    if (nextId) {
      nextMsg = conversation.messages.find(m => m.id === nextId);
    } else {
      const currentIndex = conversation.messages.findIndex(m => m.id === currentMessageId);
      nextMsg = conversation.messages[currentIndex + 1];
    }

    console.log(`[CONV DIAGNOSTIC] nextNodeId: ${nextMsg?.id || 'NONE'}`);

    if (nextMsg) {
      const hostMessage: ChatMessage = { 
        role: nextMsg.role, 
        text: nextMsg.text, 
        english: (nextMsg as any).english, 
        id: nextMsg.id 
      };
      
      // Update history and state atomically
      setChatHistory(prev => [...prev, userMessage, hostMessage]);
      setCurrentMessageId(nextMsg.id);
      void Tts.speak(nextMsg.text);
    } else {
      // No more messages in array - treat as end if not explicit
      setChatHistory(prev => [...prev, userMessage]);
      console.warn("No next message found in sequence. Ending conversation.");
      setTimeout(() => {
        navigate(`/scenarios/${scenarioId}/lesson/l1/complete`, { replace: true });
      }, 500);
    }

    // Reset state for next turn
    setSelectedChoice(null);
    setIsCorrect(null);
  };

  // Keyboard navigation
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        navigate(`/scenarios/${scenarioId}`);
        return;
      }
      
      if (e.key.toLowerCase() === 't') {
        if (isLatestMessageRevealed) {
          setShowTranslation(prev => !prev);
        }
        return;
      }
      
      if (e.key === ' ') {
        e.preventDefault();
        if (currentMessage) {
          void Tts.speak(currentMessage.text);
        }
        return;
      }

      if (e.key === 'Enter') {
        if (isCorrect === true) {
          handleContinue();
        }
        return;
      }

      // Choice selection (1-4)
      if (isCorrect !== true && randomizedChoices.length > 0) {
        const num = parseInt(e.key, 10);
        if (!isNaN(num) && num >= 1 && num <= randomizedChoices.length) {
          handleChoice(randomizedChoices[num - 1]);
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [navigate, scenarioId, showTranslation, currentMessage, isCorrect, randomizedChoices, handleContinue, handleChoice, isLatestMessageRevealed]);


  if (!scenario || !conversation) return null;

  return (
    <Screen style={{ padding: 0 }}>
      <div style={{
        padding: spacing.md, 
        borderBottom: `1px solid ${colors.border}`, 
        backgroundColor: colors.surface,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        gap: spacing.md,
        zIndex: 5
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: spacing.md }}>
          <button 
            onClick={() => navigate(`/scenarios/${scenarioId}`)}
            style={{ background: 'none', border: 'none', cursor: 'pointer', color: colors.primary, padding: 0 }}
            title="Exit (Esc)"
          >
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
              <path d="M19 12H5M12 19l-7-7 7-7"/>
            </svg>
          </button>
          <div>
            <h2 style={{fontSize: 16, margin: 0, color: colors.primary, fontWeight: 900}}>{conversation.title}</h2>
            <p style={{fontSize: 12, color: colors.textSecondary, margin: 0, fontWeight: 700}}>Scripted Practice</p>
          </div>
        </div>

        {/* Runtime Diagnostics */}
        <div style={{ position: 'absolute', top: 60, left: 10, backgroundColor: 'rgba(0,0,0,0.7)', color: 'white', padding: '4px 8px', borderRadius: 4, fontSize: 10, zIndex: 10, pointerEvents: 'none' }}>
           NODE: {currentMessageId} | HISTORY: {chatHistory.length}
        </div>

        <div style={{ display: 'flex', gap: spacing.sm }}>

          <button
            onClick={() => { if (currentMessage) void Tts.speak(currentMessage.text); }}
            style={{ background: colors.chipBg, border: 'none', borderRadius: 8, padding: '4px 8px', fontSize: 12, fontWeight: 700, cursor: 'pointer', color: colors.primary }}
            title="Replay Audio (Space)"
          >
            🔊 Space
          </button>
          <button
            onClick={() => { if (isLatestMessageRevealed) setShowTranslation(p => !p); }}
            disabled={!isLatestMessageRevealed}
            style={{ 
              background: showTranslation ? colors.accent : colors.chipBg, 
              border: 'none', 
              borderRadius: 8, 
              padding: '4px 8px', 
              fontSize: 12, 
              fontWeight: 700, 
              cursor: isLatestMessageRevealed ? 'pointer' : 'not-allowed', 
              color: showTranslation ? colors.surface : colors.primary,
              opacity: isLatestMessageRevealed ? 1 : 0.5
            }}
            title="Toggle Translation (T)"
          >
            🌐 T
          </button>
        </div>
      </div>

      <div ref={scrollRef} style={{
        flex: 1, 
        overflowY: 'auto', 
        padding: spacing.md, 
        display: 'flex', 
        flexDirection: 'column', 
        gap: spacing.lg,
        paddingBottom: 40
      }}>
        {chatHistory.map((msg, idx) => {
          const isRevealed = msg.role === 'user' || revealedMessages.has(msg.id + idx);
          
          return (
          <div
            key={msg.id + idx}
            className="fade-in"
            style={{
              alignSelf: msg.role === 'host' ? 'flex-start' : 'flex-end',
              maxWidth: '85%',
              backgroundColor: msg.role === 'host' ? colors.surface : colors.primary,
              color: msg.role === 'host' ? colors.primary : colors.onPrimary,
              padding: `${spacing.md}px ${spacing.lg}px`,
              borderRadius: msg.role === 'host' ? '20px 20px 20px 4px' : '20px 20px 4px 20px',
              boxShadow: '0 2px 8px rgba(0,0,0,0.05)',
              border: msg.role === 'host' ? `2px solid ${colors.border}` : 'none',
              fontSize: 17,
              lineHeight: '1.4',
              fontWeight: 600,
              position: 'relative'
            }}
          >
            {msg.role === 'host' && !isRevealed ? (
              <button
                onClick={() => setRevealedMessages(prev => new Set(prev).add(msg.id + idx))}
                style={{
                  background: 'none',
                  border: 'none',
                  color: colors.primary,
                  fontWeight: 800,
                  fontSize: 16,
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 8,
                  padding: 0
                }}
              >
                <span style={{ fontSize: 24 }}>🎧</span> Show Text
              </button>
            ) : (
              <>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: spacing.md }}>
                  <div style={{ flex: 1 }}>{msg.text}</div>
                  {msg.role === 'user' && (
                    <button 
                      onClick={() => void Tts.speak(msg.text)}
                      style={{ 
                        background: 'rgba(255,255,255,0.2)', 
                        border: 'none', 
                        borderRadius: '50%', 
                        width: 28, 
                        height: 28, 
                        display: 'flex', 
                        alignItems: 'center', 
                        justifyContent: 'center', 
                        cursor: 'pointer',
                        color: 'white',
                        fontSize: 14
                      }}
                      title="Replay Audio"
                    >
                      🔊
                    </button>
                  )}
                </div>
                {showTranslation && msg.english && msg.role === 'host' && (
                  <div style={{ marginTop: 8, fontSize: 14, fontStyle: 'italic', opacity: 0.8 }}>
                    {msg.english}
                  </div>
                )}
              </>
            )}
          </div>
          );
        })}

        {isCorrect === false && selectedChoice?.feedback && (
          <div className="shake">
            <FeedbackMessage 
              type="incorrect"
              message="Non proprio..."
              explanation={selectedChoice.feedback}
            />
            {selectedChoice.hint && (
              <div style={{ marginTop: spacing.sm, padding: spacing.md, backgroundColor: 'rgba(212, 163, 115, 0.1)', borderRadius: 12, border: `1px dashed ${colors.accent}`, color: colors.primary, fontSize: 14, fontWeight: 700 }}>
                💡 Suggerimento: {selectedChoice.hint}
              </div>
            )}
          </div>
        )}

        {isCorrect === true && selectedChoice?.feedback && (
          <div className="fade-in">
            <FeedbackMessage 
              type="correct"
              message="Ottimo!"
              explanation={selectedChoice.feedback}
            />
          </div>
        )}
      </div>

      <div style={{
        padding: spacing.md, 
        backgroundColor: colors.surface, 
        borderTop: `2px solid ${colors.border}`, 
        display: 'flex', 
        flexDirection: 'column', 
        gap: spacing.md
      }}>
        {currentMessage?.choices && isCorrect !== true && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.sm }}>
            {randomizedChoices.map((choice, idx) => (
              <button
                key={idx}
                onClick={() => handleChoice(choice)}
                className={`card ${selectedChoice === choice ? 'active' : ''}`}
                style={{
                  padding: spacing.md,
                  textAlign: 'left',
                  fontSize: 16,
                  fontWeight: 700,
                  color: colors.primary,
                  border: selectedChoice === choice 
                    ? `2px solid ${isCorrect === false ? colors.error : colors.accent}` 
                    : `2px solid ${colors.border}`,
                  backgroundColor: colors.surface,
                  cursor: 'pointer',
                  opacity: selectedChoice && selectedChoice !== choice ? 0.6 : 1,
                  display: 'flex',
                  alignItems: 'center',
                  gap: spacing.sm
                }}
              >
                <span style={{ 
                  display: 'inline-flex', 
                  alignItems: 'center', 
                  justifyContent: 'center', 
                  width: 24, 
                  height: 24, 
                  borderRadius: 12, 
                  backgroundColor: colors.chipBg, 
                  fontSize: 12, 
                  fontWeight: 800 
                }}>{idx + 1}</span>
                {choice.text}
              </button>
            ))}
          </div>
        )}

        {isCorrect === true && (
          <PrimaryButton label="Continue (Enter)" onPress={handleContinue} />
        )}
      </div>
    </Screen>
  );
};

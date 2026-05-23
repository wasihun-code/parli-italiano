import React, {useCallback, useEffect, useMemo, useRef, useState} from 'react';
import {useNavigate, useParams} from 'react-router-dom';

import {PrimaryButton} from '../components/PrimaryButton';
import {Screen} from '../components/Screen';
import {generateResponse} from '../lib/llm';
import {setupDatabase, loadScenarioHeader, loadScenarioConversationVocabulary} from '../lib/db';
import {useSpeechRecognition} from '../lib/useSpeechRecognition';
import {
  assistantMessageContainsCorrection,
  buildAlpacaPrompt,
  buildConversationVocabulary,
  buildSystemMessage,
  buildGrammarMiniLessonInstruction,
} from '@shared/ai/prompt';
import {useConversationStore} from '@shared/store/conversationStore';
import {useProgressStore} from '@shared/store/progressStore';
import {Tts} from '../lib/tts';
import {colors} from '@shared/theme/colors';
import {spacing} from '@shared/theme/spacing';
import {getScenarioRoles} from '@app/data/roles';
import type {ScenarioCategory} from '@app/data/scenarios';

const scenarioCategories: ScenarioCategory[] = [
  'Travel',
  'Accommodation',
  'Dining',
  'Shopping',
  'Daily Life',
  'WorkStudy',
  'Social',
  'Culture',
  'Health',
  'Tech',
  'Miscellaneous',
  'Animals',
  'Verbs_ARE',
  'Verbs_ERE',
  'Verbs_IRE',
  'Reflexive_Verbs',
  'Adjectives',
];

function toScenarioCategory(category?: string): ScenarioCategory {
  return scenarioCategories.includes(category as ScenarioCategory)
    ? category as ScenarioCategory
    : 'Miscellaneous';
}

type TranslationState = Record<string, boolean>;

export const ConversationScreen: React.FC = () => {
  const {scenarioId} = useParams<{scenarioId: string}>();
  const navigate = useNavigate();
  const numericScenarioId = Number(scenarioId);

  const allMessages = useConversationStore(state => state.messages);
  const messages = useMemo(
    () => allMessages.filter(message => message.scenarioId === numericScenarioId),
    [allMessages, numericScenarioId],
  );
  const addMessage = useConversationStore(state => state.addMessage);
  const logUserError = useConversationStore(state => state.logUserError);
  const setSpeed = useConversationStore(state => state.setSpeed);
  const speed = useConversationStore(state => state.speed);
  const startScenario = useConversationStore(state => state.startScenario);

  const conversationUnlocked = useProgressStore(
    state => state.scenarioProgress[numericScenarioId]?.conversationUnlocked ?? false,
  );

  const [scenarioTitle, setScenarioTitle] = useState('Conversazione');
  const [roles, setRoles] = useState({aiRole: 'tutor', userRole: 'learner'});
  const [allowedVocabulary, setAllowedVocabulary] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [showTextInput, setShowTextInput] = useState(false);
  const [inputText, setInputText] = useState('');
  const [generating, setGenerating] = useState(false);
  const [voiceStatus, setVoiceStatus] = useState('Tocca per parlare');
  const [userMessageCount, setUserMessageCount] = useState(0);
  const [errorMessage, setErrorMessage] = useState<string>();
  const [translations, setTranslations] = useState<TranslationState>({});

  const scrollRef = useRef<HTMLDivElement>(null);
  const lastTranscript = useRef('');
  const introStarted = useRef(false);
  const speech = useSpeechRecognition('it-IT');

  useEffect(() => {
    if (messages.length > 0) {
      const lastMessage = messages[messages.length - 1];
      if (lastMessage.role === 'assistant') {
        Tts.speak(lastMessage.text);
      }
    }
  }, [messages]);

  const systemPrompt = useMemo(
    () => {
      let prompt = buildSystemMessage(scenarioTitle, roles.aiRole, allowedVocabulary);
      if (speed === 'lento') {
        prompt += ' Parla lentamente.';
      }
      return prompt;
    },
    [allowedVocabulary, roles.aiRole, scenarioTitle, speed],
  );

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages, generating, errorMessage]);

  useEffect(() => {
    let cancelled = false;

    async function prepare(): Promise<void> {
      if (!conversationUnlocked) {
        setLoading(false);
        return;
      }

      try {
        await setupDatabase();
        const [header, vocabulary] = await Promise.all([
          loadScenarioHeader(numericScenarioId),
          loadScenarioConversationVocabulary(numericScenarioId),
        ]);

        if (cancelled) return;

        setScenarioTitle(header?.title ?? `Scenario ${numericScenarioId}`);
        setRoles(getScenarioRoles(numericScenarioId, toScenarioCategory(header?.category)));
        setAllowedVocabulary(buildConversationVocabulary(vocabulary));
        startScenario(numericScenarioId);
      } catch (error) {
        if (!cancelled) {
          setErrorMessage(error instanceof Error ? error.message : 'Impossibile iniziare la conversazione.');
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    prepare();
    return () => {
      cancelled = true;
    };
  }, [conversationUnlocked, numericScenarioId, startScenario]);

  const [generatingStatus, setGeneratingStatus] = useState<string>('');

  const sendPromptToAntonio = useCallback(
    async (userText: string): Promise<void> => {
      const rawMessages = useConversationStore.getState().messages;
      const historyMessages = rawMessages.filter(
        message => message.scenarioId === numericScenarioId && (message.role === 'assistant' || message.role === 'user')
      );
      
      if (historyMessages.length > 0) {
        const lastMsg = historyMessages[historyMessages.length - 1];
        if (lastMsg.role === 'user' && lastMsg.text === userText) {
          historyMessages.pop();
        }
      }

      setGeneratingStatus('Antonio sta pensando...');
      
      // For Alpaca fine-tuned model, we should concatenate history into a single string 
      // or use a specific format that the model can understand as context.
      // Since it was trained on single turns, the best way to do multi-turn is to 
      // pass the history inside the "Input" block.
      
      const historyStr = historyMessages.map(msg => 
        `${msg.role === 'assistant' ? 'Antonio' : 'User'}: ${msg.text}`
      ).join('\n');

      const fullInput = historyStr ? `${historyStr}\nUser: ${userText}` : userText;

      const assistantText = await generateResponse([
        { role: 'system', content: systemPrompt },
        { role: 'user', content: fullInput }
      ]);

      addMessage({
        scenarioId: numericScenarioId,
        role: 'assistant',
        text: assistantText,
      });

      if (assistantMessageContainsCorrection(assistantText)) {
        logUserError({
          scenarioId: numericScenarioId,
          sourceText: userText,
          correction: assistantText,
          explanation: 'Antonio ha incluso una correzione nella risposta.',
        });
      }
    },
    [addMessage, logUserError, numericScenarioId, systemPrompt],
  );

  useEffect(() => {
    let cancelled = false;

    if (
      loading ||
      !conversationUnlocked ||
      allowedVocabulary.length === 0 ||
      messages.length > 0 ||
      introStarted.current
    ) {
      return;
    }

    introStarted.current = true;
    setGenerating(true);
    setErrorMessage(undefined);

    const getInitialGreeting = async (): Promise<string> => {
      setGeneratingStatus('Antonio si sta preparando...');
      const response = await generateResponse([
        { role: 'system', content: systemPrompt },
        { role: 'user', content: 'Inizia la conversazione.' }
      ]);
      return response;
    };

    getInitialGreeting()
      .then(text => {
        if (cancelled) return;
        addMessage({
          scenarioId: numericScenarioId,
          role: 'assistant',
          text: text,
        });
      })
      .catch(error => {
        if (cancelled) return;
        const message =
          error instanceof Error
            ? error.message
            : 'Antonio non ha potuto iniziare questo scenario.';
        setErrorMessage(message);
        introStarted.current = false;
      })
      .finally(() => {
        setGenerating(false);
        setGeneratingStatus('');
      });

    return () => {
      cancelled = true;
    };
  }, [
    addMessage,
    allowedVocabulary.length,
    conversationUnlocked,
    loading,
    messages.length,
    numericScenarioId,
    systemPrompt,
  ]);

  const sendUserMessage = useCallback(
    async (overrideText?: string): Promise<void> => {
      const userText = (overrideText ?? inputText).trim();
      if (!userText || generating || loading) {
        return;
      }

      setGenerating(true);
      setErrorMessage(undefined);
      setInputText('');
      addMessage({scenarioId: numericScenarioId, role: 'user', text: userText});

      try {
        await sendPromptToAntonio(userText);
        const nextCount = userMessageCount + 1;
        setUserMessageCount(nextCount);

        if (nextCount % 6 === 0) {
          const historyMessages = useConversationStore
            .getState()
            .messages.filter(
              message =>
                message.scenarioId === numericScenarioId &&
                (message.role === 'assistant' || message.role === 'user'),
            );
          
          const historyStr = historyMessages.map(msg => 
            `${msg.role === 'assistant' ? 'Antonio' : 'User'}: ${msg.text}`
          ).join('\n');

          const lessonInput = `${historyStr}\nUser: ${buildGrammarMiniLessonInstruction()}`;

          const miniLesson = await generateResponse([
            { role: 'system', content: systemPrompt },
            { role: 'user', content: lessonInput }
          ]);
          
          addMessage({
            scenarioId: numericScenarioId,
            role: 'assistant',
            text: miniLesson,
          });
        }
      } catch (error) {
        const message =
          error instanceof Error
            ? error.message
            : 'Antonio non può rispondere in questo momento.';
        setErrorMessage(message);
        addMessage({scenarioId: numericScenarioId, role: 'assistant', text: message});
      } finally {
        setGenerating(false);
        setVoiceStatus('Tocca per parlare');
      }
    },
    [
      addMessage,
      generating,
      inputText,
      loading,
      numericScenarioId,
      sendPromptToAntonio,
      systemPrompt,
      userMessageCount,
    ],
  );

  useEffect(() => {
    const transcript = speech.transcript.trim();
    if (!speech.listening && transcript && transcript !== lastTranscript.current) {
      lastTranscript.current = transcript;
      void sendUserMessage(transcript);
    }
  }, [sendUserMessage, speech.listening, speech.transcript]);

  const handleToggleVoice = async (): Promise<void> => {
    if (speech.listening) {
      speech.stop();
      setVoiceStatus('Tocca per parlare');
      return;
    }

    setErrorMessage(undefined);
    setVoiceStatus('In ascolto...');
    speech.start();
  };

  const handleToggleTranslation = useCallback(async (messageId: string): Promise<void> => {
    const message = useConversationStore.getState().messages.find(m => m.id === messageId);
    if (message && !message.translation && !translations[messageId]) {
      setGeneratingStatus('Traduzione in corso...');
      setGenerating(true);
      try {
        const translationPrompt = buildAlpacaPrompt(
          'Translate the following Italian text to English. Only reply with the translation.',
          message.text
        );
        
        const english = await generateResponse([{ role: 'user', content: translationPrompt }]);
        
        // Update the message in the store with the translation
        useConversationStore.setState(state => ({
          messages: state.messages.map(m => 
            m.id === messageId ? { ...m, translation: english } : m
          )
        }));
      } catch (e) {
        console.error('On-demand translation failed', e);
      } finally {
        setGenerating(false);
        setGeneratingStatus('');
      }
    }

    setTranslations(current => ({
      ...current,
      [messageId]: !current[messageId],
    }));
  }, [translations]);

  if (!conversationUnlocked) {
    return (
      <Screen style={{ justifyContent: 'center' }}>
        <div className="card fade-in" style={{textAlign: 'center', padding: spacing.xl}}>
          <div style={{ fontSize: 64, marginBottom: spacing.md }}>🔒</div>
          <h1 style={{color: colors.primary}}>Conversazione Bloccata</h1>
          <p style={{ color: colors.textSecondary, marginBottom: spacing.lg }}>Completa tutte le fasi di allenamento per sbloccare la conversazione con Antonio.</p>
          <PrimaryButton label="Torna agli Scenari" onPress={() => navigate('/scenarios')} />
        </div>
      </Screen>
    );
  }

  return (
    <Screen style={{ paddingLeft: 0, paddingRight: 0, paddingBottom: 0, backgroundColor: colors.bg }}>
      <div style={{
        padding: spacing.md, 
        borderBottom: `1px solid ${colors.border}`, 
        backgroundColor: 'rgba(250, 249, 246, 0.95)', 
        backdropFilter: 'blur(8px)',
        flexShrink: 0,
        display: 'flex',
        alignItems: 'center',
        gap: spacing.md,
        zIndex: 5
      }}>
        <div style={{ 
          width: 48, 
          height: 48, 
          borderRadius: 24, 
          backgroundColor: colors.primary, 
          display: 'flex', 
          alignItems: 'center', 
          justifyContent: 'center',
          fontSize: 24,
          boxShadow: '0 4px 12px rgba(78, 52, 46, 0.2)'
        }}>
          👨🏻‍🏫
        </div>
        <div style={{ flex: 1 }}>
          <h2 style={{fontSize: 18, margin: 0, color: colors.primary}}>Antonio</h2>
          <p style={{fontSize: 12, color: colors.textSecondary, margin: 0, textTransform: 'uppercase', fontWeight: 900, letterSpacing: 1.5}}>
            {roles.aiRole} • {scenarioTitle}
          </p>
        </div>
        <div style={{display: 'flex', gap: spacing.xs}}>
          <button
            onClick={() => setSpeed(speed === 'lento' ? 'normale' : 'lento')}
            style={{
              border: `2px solid ${colors.border}`,
              borderRadius: 12,
              backgroundColor: colors.surface,
              color: colors.primary,
              padding: '6px 10px',
              fontWeight: 800,
              fontSize: 11,
              cursor: 'pointer',
            }}
          >
            {speed === 'lento' ? 'LENTO' : 'NORMALE'}
          </button>
          <button
            onClick={() => {
              if (window.confirm('Vuoi resettare questa conversazione?')) {
                useConversationStore.getState().clearScenario(numericScenarioId);
                introStarted.current = false;
                window.location.reload();
              }
            }}
            style={{
              border: `2px solid ${colors.border}`,
              borderRadius: 12,
              backgroundColor: colors.surface,
              color: colors.error,
              padding: '6px 10px',
              fontWeight: 800,
              fontSize: 11,
              cursor: 'pointer',
            }}
          >
            RESET
          </button>
        </div>
      </div>

      <div ref={scrollRef} style={{
        flex: 1, 
        minHeight: 0, 
        overflowY: 'auto', 
        padding: spacing.md, 
        display: 'flex', 
        flexDirection: 'column', 
        gap: spacing.lg,
        paddingBottom: 40
      }}>
        {messages.map(message => {
          const showingEnglish = translations[message.id];
          const isAi = message.role === 'assistant';
          const displayText =
            isAi && showingEnglish
              ? message.translation ?? 'La traduzione inglese non è stata inclusa.'
              : message.text;
          
          return (
            <div
              key={message.id}
              className="fade-in"
              style={{
                alignSelf: isAi ? 'flex-start' : 'flex-end',
                maxWidth: '85%',
                display: 'flex',
                flexDirection: 'column',
                gap: 4,
                flexShrink: 0,
              }}
            >
              <div
                style={{
                  backgroundColor: isAi ? colors.surface : colors.primary,
                  color: isAi ? colors.primary : colors.onPrimary,
                  padding: `${spacing.md}px ${spacing.lg}px`,
                  borderRadius: isAi ? '20px 20px 20px 4px' : '20px 20px 4px 20px',
                  boxShadow: isAi ? '0 4px 15px rgba(78, 52, 46, 0.05)' : '0 4px 15px rgba(78, 52, 46, 0.15)',
                  border: isAi ? `2px solid ${colors.border}` : 'none',
                  position: 'relative',
                  fontSize: 17,
                  lineHeight: '1.5',
                  fontWeight: isAi ? 600 : 500
                }}
              >
                <div style={{whiteSpace: 'pre-wrap'}}>{displayText}</div>
                {isAi && (
                  <button
                    onClick={() => handleToggleTranslation(message.id)}
                    style={{
                      marginTop: 8,
                      border: 'none',
                      background: 'none',
                      color: colors.accent,
                      fontSize: 12,
                      fontWeight: 800,
                      cursor: 'pointer',
                      padding: 0,
                      display: 'flex',
                      alignItems: 'center',
                      gap: 4,
                      textTransform: 'uppercase',
                      letterSpacing: 0.5
                    }}
                  >
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                      <path d="m5 8 6 6 6-6"/>
                    </svg>
                    {showingEnglish ? 'Mostra Italiano' : 'Traduci'}
                  </button>
                )}
              </div>
            </div>
          );
        })}
        {errorMessage && (
          <div className="shake" style={{
            color: colors.error, 
            fontWeight: 800, 
            textAlign: 'center',
            backgroundColor: 'rgba(158, 42, 43, 0.05)',
            padding: 12,
            borderRadius: 12,
            border: `2px solid ${colors.error}`
          }}>
            {errorMessage}
          </div>
        )}
        {(generating || speech.listening) && (
          <div style={{
            display: 'flex', 
            alignItems: 'center', 
            gap: 8, 
            alignSelf: 'flex-start',
            backgroundColor: 'rgba(78, 52, 46, 0.05)',
            padding: '8px 16px',
            borderRadius: 20,
            fontSize: 14,
            fontWeight: 700,
            color: colors.textSecondary
          }}>
            <div className="bounce" style={{ display: 'flex', gap: 4 }}>
              <div style={{ width: 6, height: 6, borderRadius: 3, backgroundColor: colors.accent }}></div>
              <div style={{ width: 6, height: 6, borderRadius: 3, backgroundColor: colors.accent, animationDelay: '0.1s' }}></div>
              <div style={{ width: 6, height: 6, borderRadius: 3, backgroundColor: colors.accent, animationDelay: '0.2s' }}></div>
            </div>
            {generating ? (generatingStatus || 'Antonio sta scrivendo...') : voiceStatus}
          </div>
        )}
      </div>

      <div style={{
        flexShrink: 0, 
        padding: spacing.md, 
        paddingBottom: `calc(${spacing.md}px + env(safe-area-inset-bottom))`,
        backgroundColor: colors.surface, 
        borderTop: `2px solid ${colors.border}`, 
        display: 'flex', 
        flexDirection: 'column', 
        alignItems: 'center', 
        gap: spacing.md,
        zIndex: 5
      }}>
        {!showTextInput ? (
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: spacing.sm, width: '100%' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: spacing.xl }}>
               <button
                aria-label="Type instead"
                onClick={() => setShowTextInput(true)}
                style={{
                  width: 56,
                  height: 56,
                  borderRadius: 28,
                  backgroundColor: colors.chipBg,
                  color: colors.primary,
                  border: 'none',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                }}
              >
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>
                </svg>
              </button>

              <button
                aria-label="Toggle voice"
                onClick={handleToggleVoice}
                disabled={loading || generating || Boolean(speech.error)}
                style={{
                  width: 80,
                  height: 80,
                  borderRadius: 40,
                  backgroundColor: speech.listening ? colors.error : colors.primary,
                  color: 'white',
                  border: 'none',
                  cursor: loading || generating || speech.error ? 'not-allowed' : 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  boxShadow: speech.listening ? `0 0 24px ${colors.error}88` : '0 8px 25px rgba(78, 52, 46, 0.2)',
                  transform: speech.listening ? 'scale(1.1)' : 'scale(1)',
                  transition: 'all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)'
                }}
              >
                {speech.listening ? (
                  <div style={{ width: 24, height: 24, backgroundColor: 'white', borderRadius: 4 }} />
                ) : (
                  <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="22"/>
                  </svg>
                )}
              </button>

              <button
                aria-label="Non capisco"
                onClick={() => sendUserMessage('non capisco')}
                disabled={loading || generating}
                style={{
                  width: 56,
                  height: 56,
                  borderRadius: 28,
                  backgroundColor: colors.chipBg,
                  color: colors.primary,
                  border: 'none',
                  cursor: loading || generating ? 'not-allowed' : 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                }}
              >
                <span style={{ fontSize: 20, fontWeight: 900 }}>?</span>
              </button>
            </div>
            
            <span style={{fontWeight: 900, color: speech.listening ? colors.error : colors.primary, fontSize: 14, letterSpacing: 0.5}}>
              {speech.error ? 'Errore microfono' : voiceStatus.toUpperCase()}
            </span>
          </div>
        ) : (
          <div className="fade-in" style={{width: '100%', display: 'flex', gap: spacing.sm, alignItems: 'center'}}>
            <button 
              aria-label="Close text input"
              onClick={() => setShowTextInput(false)} 
              style={{
                width: 40, 
                height: 40, 
                borderRadius: 20, 
                background: colors.chipBg, 
                border: 'none', 
                color: colors.textSecondary,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                cursor: 'pointer'
              }}
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                <path d="M18 6L6 18M6 6l12 12"/>
              </svg>
            </button>
            <input
              autoFocus
              value={inputText}
              onChange={event => setInputText(event.target.value)}
              onKeyDown={event => event.key === 'Enter' && sendUserMessage()}
              placeholder="Scrivi in italiano..."
              style={{
                flex: 1, 
                minWidth: 0, 
                padding: `${spacing.md}px ${spacing.lg}px`, 
                borderRadius: 24, 
                border: `2px solid ${colors.border}`, 
                outline: 'none',
                fontSize: 16,
                fontWeight: 600,
                color: colors.primary,
                backgroundColor: colors.bg
              }}
            />
            <button
              aria-label="Send message"
              onClick={() => sendUserMessage()}
              disabled={generating || !inputText.trim()}
              style={{
                width: 48, 
                height: 48, 
                borderRadius: 24, 
                backgroundColor: colors.accent, 
                color: 'white', 
                border: 'none',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                cursor: generating || !inputText.trim() ? 'not-allowed' : 'pointer',
                boxShadow: '0 4px 10px rgba(212, 163, 115, 0.3)'
              }}
            >
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                <line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>
              </svg>
            </button>
          </div>
        )}
      </div>
    </Screen>
  );
};

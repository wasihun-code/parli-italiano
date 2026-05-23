import { useUserSettingsStore } from '../store/userSettingsStore';
import { db } from './db';

let cachedVoices: SpeechSynthesisVoice[] = [];
let currentAudio: HTMLAudioElement | undefined;

function loadVoices(): SpeechSynthesisVoice[] {
  if (typeof window === 'undefined' || !window.speechSynthesis) {
    return [];
  }

  cachedVoices = window.speechSynthesis.getVoices();
  return cachedVoices;
}

if (typeof window !== 'undefined' && window.speechSynthesis) {
  window.speechSynthesis.onvoiceschanged = loadVoices;
  loadVoices();
}

function findItalianVoice(): SpeechSynthesisVoice | undefined {
  const voices = cachedVoices.length > 0 ? cachedVoices : loadVoices();
  return (
    voices.find(voice => voice.lang.toLocaleLowerCase('it-IT').startsWith('it')) ||
    voices.find(voice => voice.name.toLocaleLowerCase('it-IT').includes('italian'))
  );
}

async function speakWithBrowserItalianVoice(text: string): Promise<void> {
  if (typeof window === 'undefined' || !window.speechSynthesis) {
    throw new Error('Speech synthesis not supported');
  }

  const voice = findItalianVoice();
  if (!voice) {
    throw new Error('Italian voice not found');
  }

  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.voice = voice;
  utterance.lang = 'it-IT';
  utterance.pitch = 1;
  utterance.rate = 0.9;

  return new Promise((resolve, reject) => {
    utterance.onend = () => resolve();
    utterance.onerror = (e) => reject(e);
    window.speechSynthesis.speak(utterance);
  });
}

async function fetchGoogleTts(text: string): Promise<Blob> {
  const token = localStorage.getItem('auth_token');
  const baseUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';
  const url = `${baseUrl}/tts-proxy/?q=${encodeURIComponent(text)}`;
  
  const response = await fetch(url, {
    headers: {
      ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
    }
  });

  if (!response.ok) {
    throw new Error('TTS proxy request failed');
  }
  return await response.blob();
}

async function speakWithApiTts(text: string): Promise<void> {
  // Check cache first
  const cached = await db.tts_cache.get(text);
  let audioBlob: Blob;

  if (cached) {
    audioBlob = cached.audio;
  } else {
    audioBlob = await fetchGoogleTts(text);
    // Save to cache
    await db.tts_cache.put({
      text,
      audio: audioBlob,
      updated_at: new Date().toISOString(),
    });
  }

  const url = URL.createObjectURL(audioBlob);
  currentAudio = new Audio(url);

  return new Promise((resolve, reject) => {
    if (!currentAudio) {
      reject(new Error('Unable to create audio element.'));
      return;
    }

    currentAudio.onended = () => {
      URL.revokeObjectURL(url);
      currentAudio = undefined;
      resolve();
    };
    currentAudio.onerror = () => {
      URL.revokeObjectURL(url);
      currentAudio = undefined;
      reject(new Error('API TTS audio playback failed.'));
    };
    currentAudio.play().catch(reject);
  });
}

export async function speak(text: string): Promise<void> {
  const phrase = text.trim();
  if (!phrase) {
    return;
  }

  const { ttsProvider, soundEnabled } = useUserSettingsStore.getState();
  if (!soundEnabled) {
    return;
  }

  if (ttsProvider === 'api') {
    try {
      await speakWithApiTts(phrase);
    } catch (error) {
      console.warn('API TTS failed, falling back to browser:', error);
      try {
        await speakWithBrowserItalianVoice(phrase);
      } catch (browserError) {
        console.error('Browser TTS also failed:', browserError);
      }
    }
  } else {
    try {
      await speakWithBrowserItalianVoice(phrase);
    } catch (error) {
      console.error('Browser TTS failed:', error);
    }
  }
}

export const Tts = {
  speak,
  stop: () => {
    if (typeof window !== 'undefined' && window.speechSynthesis) {
      window.speechSynthesis.cancel();
    }
    if (currentAudio) {
      currentAudio.pause();
      currentAudio = undefined;
    }
  },
};

export default Tts;

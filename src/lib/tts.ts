import {EdgeTTS} from 'edge-tts-universal/browser';

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

function speakWithBrowserItalianVoice(text: string): Promise<boolean> {
  if (typeof window === 'undefined' || !window.speechSynthesis) {
    return Promise.resolve(false);
  }

  const voice = findItalianVoice();
  if (!voice) {
    return Promise.resolve(false);
  }

  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.voice = voice;
  utterance.lang = 'it-IT';
  utterance.pitch = 1;
  utterance.rate = 0.9;

  return new Promise(resolve => {
    utterance.onend = () => resolve(true);
    utterance.onerror = () => resolve(false);
    window.speechSynthesis.speak(utterance);
  });
}

async function speakWithEdgeTts(text: string): Promise<void> {
  const edgeTts = new EdgeTTS(text, 'it-IT-ElsaNeural');
  const response = await edgeTts.synthesize();
  const url = URL.createObjectURL(response.audio);
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
      reject(new Error('Edge TTS audio playback failed.'));
    };
    currentAudio.play().catch(reject);
  });
}

export async function speak(text: string): Promise<void> {
  const phrase = text.trim();
  if (!phrase) {
    return;
  }

  const spokeWithBrowser = await speakWithBrowserItalianVoice(phrase);
  if (spokeWithBrowser) {
    return;
  }

  await speakWithEdgeTts(phrase);
}

export const Tts = {
  speak,
  stop: () => {
    if (typeof window !== 'undefined' && window.speechSynthesis) {
      window.speechSynthesis.cancel();
    }
    currentAudio?.pause();
    currentAudio = undefined;
  },
};

export default Tts;

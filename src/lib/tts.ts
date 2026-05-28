import { useUserSettingsStore } from '../store/userSettingsStore';
import { resolveAudioPath, type ScenarioAudio } from '../utils/audio';

let currentAudio: HTMLAudioElement | undefined;

async function playAudioFile(url: string): Promise<void> {
  if (currentAudio) {
    currentAudio.pause();
    currentAudio = undefined;
  }

  currentAudio = new Audio(url);
  return new Promise((resolve, reject) => {
    if (!currentAudio) {
      reject(new Error('Unable to create audio element.'));
      return;
    }

    currentAudio.onended = () => {
      currentAudio = undefined;
      resolve();
    };
    currentAudio.onerror = () => {
      currentAudio = undefined;
      reject(new Error(`Audio playback failed for: ${url}`));
    };
    currentAudio.play().catch(reject);
  });
}

/**
 * Plays pre-recorded Italian audio from the production corpus.
 * Synthetic TTS (Browser/API) is no longer supported.
 * If audio metadata is missing, it attempts to resolve the deterministic asset path from text.
 */
export async function speak(text: string, audio?: string | ScenarioAudio): Promise<void> {
  const { soundEnabled } = useUserSettingsStore.getState();
  if (!soundEnabled) {
    return;
  }

  const prerecordedUrl = await resolveAudioPath(audio, text);

  if (prerecordedUrl) {
    try {
      await playAudioFile(prerecordedUrl);
    } catch (error) {
      // Asset might be missing from disk even if path was resolved
      console.debug(`[Deterministic Audio] Asset missing or failed to load: ${prerecordedUrl}`);
    }
  } else {
    console.error(`[Deterministic Audio] Unable to resolve audio asset for: "${text.substring(0, 50)}..."`);
  }
}

export const Tts = {
  speak,
  stop: () => {
    if (currentAudio) {
      currentAudio.pause();
      currentAudio = undefined;
    }
  },
};

export default Tts;

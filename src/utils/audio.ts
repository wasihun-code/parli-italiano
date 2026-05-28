/**
 * Production schema for audio metadata.
 */
export type ScenarioAudio = {
  italian: string;
};

/**
 * Generates a deterministic 12-char SHA-1 hash for text + voice.
 * Matches the logic in scripts/audio_manager.py
 */
export async function getAudioHash(text: string, voiceId: string = 'elsa'): Promise<string> {
  const msgUint8 = new TextEncoder().encode(`${text.trim()}|${voiceId}`);
  const hashBuffer = await crypto.subtle.digest('SHA-1', msgUint8);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  return hashHex.substring(0, 12);
}

/**
 * Resolves an audio path from the corpus metadata.
 * Supports legacy (string), production (object), and automatic hashing for plain text.
 */
export async function resolveAudioPath(
  audio?: string | ScenarioAudio, 
  textFallback?: string
): Promise<string | undefined> {
  if (!audio && !textFallback) return undefined;
  
  let path: string | undefined;
  
  if (typeof audio === 'string' && audio.startsWith('/audio/')) {
    path = audio;
  } else if (typeof audio === 'object' && audio.italian) {
    path = audio.italian;
  } else {
    // If no valid path is provided, but we have text, generate the deterministic path
    const textToHash = typeof audio === 'string' ? audio : textFallback;
    if (textToHash) {
      const hash = await getAudioHash(textToHash);
      path = `/audio/${hash}.opus`;
    }
  }
  
  // Final validation
  if (typeof path === 'string' && path.startsWith('/audio/')) {
    return path;
  }
  
  return undefined;
}

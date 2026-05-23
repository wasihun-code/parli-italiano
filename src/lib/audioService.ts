
import { useUserSettingsStore } from '../store/userSettingsStore';

class AudioService {
  private context: AudioContext | null = null;

  private isSoundEnabled() {
    return useUserSettingsStore.getState().soundEnabled;
  }

  private initContext() {
    if (!this.isSoundEnabled()) return;
    if (!this.context) {
      const AudioCtx = window.AudioContext || (window as any).webkitAudioContext;
      if (!AudioCtx) return;
      this.context = new AudioCtx();
    }
    if (this.context && this.context.state === 'suspended') {
      this.context.resume();
    }
  }

  private playTone(freq: number, type: OscillatorType, duration: number, volume: number = 0.1) {
    if (!this.isSoundEnabled()) return;
    this.initContext();
    if (!this.context) return;

    const osc = this.context.createOscillator();
    const gain = this.context.createGain();

    osc.type = type;
    osc.frequency.setValueAtTime(freq, this.context.currentTime);

    gain.gain.setValueAtTime(volume, this.context.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.0001, this.context.currentTime + duration);

    osc.connect(gain);
    gain.connect(this.context.destination);

    osc.start();
    osc.stop(this.context.currentTime + duration);
  }

  playCorrect() {
    this.playTone(523.25, 'sine', 0.2); // C5
    setTimeout(() => this.playTone(659.25, 'sine', 0.3), 100); // E5
  }

  playIncorrect() {
    this.playTone(200, 'sine', 0.2, 0.05); // Short soft buzz
  }

  playLevelUp() {
    this.playTone(440, 'triangle', 0.2);
    setTimeout(() => this.playTone(554.37, 'triangle', 0.2), 100);
    setTimeout(() => this.playTone(659.25, 'triangle', 0.4), 200);
  }

  playComplete() {
    const tones = [523.25, 659.25, 783.99, 1046.50];
    tones.forEach((freq, i) => {
      setTimeout(() => this.playTone(freq, 'sine', 0.5), i * 150);
    });
  }

  playClick() {
    this.playTone(800, 'sine', 0.05, 0.05);
  }
}

export const audioService = new AudioService();

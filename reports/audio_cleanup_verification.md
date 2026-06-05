# Audio Cleanup Verification Report

## Investigation Findings

The previous cleanup report flagged 44,785 files in `public/audio/` as "orphaned" because they were not explicitly referenced in the `audio: { italian: "..." }` properties within the generated curriculum JSON files.

A deep analysis reveals that these files are **NOT ORPHANED** and must **NOT** be deleted.

### 1. Deterministic Hashing & Runtime Resolver
The application relies on a deterministic hashing strategy implemented in `src/utils/audio.ts`:

```typescript
export async function resolveAudioPath(
  audio?: string | ScenarioAudio, 
  textFallback?: string
): Promise<string | undefined> {
  // ...
  if (textToHash) {
    const hash = await getAudioHash(textToHash);
    path = `/audio/${hash}.opus`;
  }
  // ...
}
```

If a vocabulary item, phrase, or sentence lacks explicit audio metadata, the frontend dynamically hashes the string (e.g., `SHA1("text|elsa")`) and attempts to load the corresponding 12-character hex `.opus` file from `public/audio/`.

### 2. Curriculum Analysis
A scan of all 116 Gold Standard scenarios (`src/data/exports/**/*.json`) reveals the following:

- **Total Curriculum Items:** 57,765
- **Items with Explicit Audio Paths:** 38,862
- **Items MISSING Audio Metadata:** 18,903

**18,903 items rely entirely on the runtime resolver** to map their text to the `12-char-hash.opus` format present on disk.

### 3. Conclusion
The 44,785 files identified as "orphaned" are the legacy deterministic hash format required to serve audio for the 18,903 items missing metadata. Deleting these files would cause catastrophic audio failures across the application. 

**Recommendation:** DO NOT DELETE `public/audio/` files. The dataset is fully utilized and safe.

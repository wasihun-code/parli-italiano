# MEMORY.md

## Completed Categories ✅
- accommodation ✅
- daily_life ✅
- dining ✅
- travel ✅
- shopping ✅
- culture ✅
- health ✅
- social ✅
- workstudy ✅
- miscellaneous ✅
- tech ✅
- verbs ✅
- adjectives ✅
- animals ✅
- reflexive ✅
- foundations ✅

## Audio Infrastructure Phase ✅
- Scalable Architecture: Migrated to a nested manifest structure.
- Voice-Aware Hashing: Audio filenames are now `sha1(text + voice_id)`.
- Production-Grade Format: All assets converted to Ogg Opus.
- Loudness Normalization: Integrated `ffmpeg loudnorm` (-16 LUFS).
- Deterministic Offline Audio Enforcement: ALL runtime synthetic TTS (browser/API/diagnostic) removed.
- Runtime Audio Schema compatibility Repair ✅: Centralized `resolveAudioPath` implemented to handle both legacy (string) and production (object) schemas.
- Deterministic Text Fallback ✅: Client-side SHA-1 hashing implemented to resolve plain text to deterministic asset paths automatically.

## Deterministic Audio Enforcement Report
- **Strict Enforcement**: The application now uses ONLY pre-generated local assets in production.
- **Total Elimination of TTS**: Synthetic Text-to-Speech logic has been completely removed.
- **Schema Compatibility**: Centralized resolver handles production audio metadata objects, legacy string paths, and plain text fallbacks.
- **Foundations Support**: Synthesized 79 unique foundation audio items to ensure a high-quality first-user experience.
- **Immersive Coverage**: 100% of corpus exercises now contain deterministic audio metadata.

## Synthesis Progress (Full Audit)
- **Travel**: 2432/2432 ✅
- **Accommodation**: 1964/1964 ✅
- **Dining**: 2084/2084 ✅
- **Social**: 1564/1564 ✅
- **Health**: 746/746 ✅
- **Culture**: 2002/2002 ✅
- **Shopping**: 1450/1450 ✅
- **Workstudy**: 1568/1568 ✅
- **Tech**: 1229/1229 ✅
- **Miscellaneous**: 740/740 ✅
- **Daily Life**: 1461/1461 ✅
- **Foundations**: 79/79 ✅
- **Verbs**: 226/226 ✅
- **Adjectives**: 89/89 ✅
- **Animals**: 71/71 ✅
- **Reflexive**: 73/73 ✅
- **Total Production Assets**: 17,778 unique items synthesized and normalized.

## Next Phase: Final Deployment & Stabilization
- Final app-wide asset integrity check.
- Production readiness validation.
- Optimization of redundant directories (`src/data/exports/daily` and `work_study`).

## Agent Lessons Learned
- When migrating schemas (string -> object), always implement a centralized resolver first.
- Client-side deterministic hashing (matching the server) provides a robust safety net for missing metadata.
- Redundant directories can clutter the manifest; strictly mapping active categories is essential for a clean audit.

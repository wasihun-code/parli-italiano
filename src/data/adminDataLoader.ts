import { scenarioMapping } from './scenarioMapping';

const globalCertFiles = import.meta.glob('../../reports/global_certification.json', { eager: true });
const scenarioCertFiles = import.meta.glob('../../reports/*_certification.json', { eager: true });
const audioManifestFiles = import.meta.glob('../../public/audio_manifest.json', { eager: true });

export const globalCertification: any = Object.values(globalCertFiles)[0] || null;
export const audioManifest: any = Object.values(audioManifestFiles)[0] || null;

export function getScenarioCertification(scenarioId: number): any {
  const slug = scenarioMapping[scenarioId];
  if (!slug) return null;
  
  // Extract slug without 'exports/'
  const actualSlug = slug.replace('exports/', '');
  const prefix = actualSlug.replace(/\//g, '_');
  
  const key = Object.keys(scenarioCertFiles).find(k => k.includes(`${prefix}_certification.json`));
  if (key) {
    const fileContent: any = scenarioCertFiles[key];
    return fileContent.default || fileContent;
  }
  return null;
}

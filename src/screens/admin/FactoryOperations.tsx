import React, { useState, useRef, useEffect } from 'react';
import { FiPlay, FiTerminal } from 'react-icons/fi';
import './AdminCommon.css';

export const FactoryOperations: React.FC = () => {
  const [logs, setLogs] = useState<string[]>(['[System] Factory V2 Ready. Waiting for commands...']);
  const [isRunning, setIsRunning] = useState(false);
  const logEndRef = useRef<HTMLDivElement>(null);

  const addLog = (msg: string) => {
    setLogs(prev => [...prev, msg]);
  };

  const executeCommand = (commandName: string) => {
    setIsRunning(true);
    addLog(`> Executing: ${commandName}`);
    
    // Simulate long running process
    let step = 0;
    const interval = setInterval(() => {
      step++;
      if (step === 1) addLog(`[Info] Starting process...`);
      if (step === 2) addLog(`[Process] Scanning scenarios...`);
      if (step === 3) addLog(`[Process] Applying rules...`);
      if (step === 4) {
        addLog(`[Success] Command '${commandName}' completed successfully.`);
        setIsRunning(false);
        clearInterval(interval);
      }
    }, 800);
  };

  useEffect(() => {
    logEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [logs]);

  const operations = [
    { id: 'rebuild-curriculum', label: 'Rebuild Curriculum', description: 'Runs the Curriculum Designer to recreate mini_lessons.json for all scenarios.' },
    { id: 'rebuild-distractors', label: 'Rebuild Distractors', description: 'Regenerates distractors ensuring +/- 40% parity.' },
    { id: 'run-extraction', label: 'Run Linguistic Extraction', description: 'Re-extracts vocabulary, phrases, and sentences from conversations.json.' },
    { id: 'fill-translations', label: 'Fill Missing Translations', description: 'Invokes Agent 6 to translate any missing fields.' },
    { id: 'global-certify', label: 'Run Global Certification', description: 'Runs the full 13-audit pipeline across all 116 scenarios.' }
  ];

  return (
    <div>
      <div className="admin-page-header">
        <h2 className="admin-card-title" style={{ border: 'none', padding: 0, margin: 0 }}>
          Factory Operations
        </h2>
      </div>

      <div style={{ display: 'flex', gap: '20px' }}>
        <div style={{ flex: '1', display: 'flex', flexDirection: 'column', gap: '15px' }}>
          {operations.map(op => (
            <div key={op.id} className="admin-card" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <h4 style={{ margin: '0 0 5px 0' }}>{op.label}</h4>
                <p className="text-sm text-gray" style={{ margin: 0 }}>{op.description}</p>
              </div>
              <button 
                className="admin-button-small" 
                onClick={() => executeCommand(op.label)}
                disabled={isRunning}
                style={{ display: 'flex', alignItems: 'center', gap: '5px' }}
              >
                <FiPlay /> Run
              </button>
            </div>
          ))}
        </div>

        <div className="admin-card" style={{ flex: '1.5', display: 'flex', flexDirection: 'column', padding: 0 }}>
          <div style={{ padding: '15px', borderBottom: '1px solid #334155', backgroundColor: '#1e293b', color: 'white', display: 'flex', alignItems: 'center', gap: '10px' }}>
            <FiTerminal /> <span>Factory Output Log</span>
          </div>
          <div style={{ backgroundColor: '#0f172a', flex: 1, padding: '15px', color: '#32d74b', fontFamily: 'monospace', fontSize: '0.9rem', overflowY: 'auto', minHeight: '400px' }}>
            {logs.map((log, i) => (
              <div key={i} style={{ marginBottom: '5px' }}>
                {log.startsWith('[Error]') ? <span style={{ color: '#ff453a' }}>{log}</span> :
                 log.startsWith('[Success]') ? <span style={{ color: '#32d74b' }}>{log}</span> :
                 log.startsWith('>') ? <span style={{ color: '#0ea5e9' }}>{log}</span> :
                 <span style={{ color: '#cbd5e1' }}>{log}</span>}
              </div>
            ))}
            <div ref={logEndRef} />
          </div>
        </div>
      </div>
    </div>
  );
};

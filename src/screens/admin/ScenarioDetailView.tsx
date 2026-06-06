import React, { useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { FiArrowLeft, FiCheckCircle } from 'react-icons/fi';
import { scenarios } from '../../data/scenarios';
import { loadProductionScenarioData } from '../../data/corpusLoader';
import { getScenarioCertification } from '../../data/adminDataLoader';
import './AdminCommon.css';

export const ScenarioDetailView: React.FC = () => {
  const { scenarioId } = useParams<{ scenarioId: string }>();
  const [activeTab, setActiveTab] = useState('Overview');

  const scenario = scenarios.find(s => s.id === Number(scenarioId));
  const data = loadProductionScenarioData(Number(scenarioId));
  const certData = getScenarioCertification(Number(scenarioId));

  if (!scenario) {
    return <div className="admin-card">Scenario not found.</div>;
  }

  const tabs = ['Overview', 'Vocabulary', 'Phrases', 'Sentences', 'Mini Lessons', 'Conversations', 'Audits'];

  const renderTable = (items: any[]) => (
    <div className="admin-table-container">
      <table className="admin-table">
        <thead><tr><th>ID</th><th>Italian</th><th>English</th><th>Audio</th></tr></thead>
        <tbody>
          {items.map(v => (
            <tr key={v.id}>
              <td>{v.id}</td>
              <td>{v.italian}</td>
              <td>{v.english}</td>
              <td>{v.audio || v.correctAnswerItalian ? '✅' : '🔍 (Hash)'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );

  return (
    <div>
      <div className="admin-page-header">
        <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
          <Link to="/admin/curriculum" className="admin-button-small">
            <FiArrowLeft />
          </Link>
          <h2 className="admin-card-title" style={{ margin: 0, border: 'none', padding: 0 }}>
            {scenario.title}
          </h2>
          <span className="admin-badge category">{scenario.category}</span>
          <span className={`admin-badge ${certData?.overall === 'PASS' ? 'success' : 'error'}`}>
            <FiCheckCircle style={{marginRight: 4}}/> {certData?.overall || 'NO DATA'}
          </span>
        </div>
      </div>

      <div className="admin-card" style={{ padding: 0, overflow: 'hidden' }}>
        <div style={{ display: 'flex', borderBottom: '1px solid #e2e8f0', backgroundColor: '#f8fafc', overflowX: 'auto' }}>
          {tabs.map(tab => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              style={{
                padding: '15px 20px',
                background: 'none',
                border: 'none',
                borderBottom: activeTab === tab ? '2px solid #0ea5e9' : '2px solid transparent',
                color: activeTab === tab ? '#0ea5e9' : '#64748b',
                fontWeight: activeTab === tab ? 600 : 500,
                cursor: 'pointer',
                fontSize: '0.95rem',
                whiteSpace: 'nowrap'
              }}
            >
              {tab}
            </button>
          ))}
        </div>

        <div style={{ padding: '20px' }}>
          {activeTab === 'Overview' && (
            <div>
              <h3>Description</h3>
              <p>{scenario.description}</p>
              
              <h3 style={{ marginTop: '20px' }}>Corpus Status</h3>
              {data ? (
                <ul style={{ lineHeight: '1.8' }}>
                  <li>Vocabulary Items: <strong>{data.vocabulary.length}</strong></li>
                  <li>Phrase Items: <strong>{data.phrases.length}</strong></li>
                  <li>Sentence Items: <strong>{data.sentences.length}</strong></li>
                  <li>Mini Lessons: <strong>{data.miniLessons?.length || 0}</strong></li>
                  <li>Scripted Conversations: <strong>{data.scriptedConversations?.length || 0}</strong></li>
                </ul>
              ) : (
                <p className="text-gray">No corpus data loaded.</p>
              )}
            </div>
          )}

          {activeTab === 'Vocabulary' && data && renderTable(data.vocabulary)}
          {activeTab === 'Phrases' && data && renderTable(data.phrases)}
          {activeTab === 'Sentences' && data && renderTable(data.sentences)}

          {activeTab === 'Mini Lessons' && (
            <div>
              {data?.miniLessons ? data.miniLessons.map((lesson: any) => (
                <div key={lesson.id} style={{ border: '1px solid #e2e8f0', padding: '15px', borderRadius: '6px', marginBottom: '15px' }}>
                  <h4 style={{ margin: '0 0 10px 0' }}>{lesson.title} ({lesson.id})</h4>
                  <p className="text-sm text-gray" style={{ margin: '0 0 15px 0' }}>Goal: {lesson.goal}</p>
                  
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '10px' }}>
                    {lesson.sections?.map((sec: any, idx: number) => (
                      <div key={idx} style={{ backgroundColor: '#f8fafc', padding: '10px', borderRadius: '4px' }}>
                        <strong>{sec.type || 'Section'}</strong>
                        <div className="text-sm text-gray">{sec.exerciseIds?.length || 0} items</div>
                      </div>
                    ))}
                  </div>
                </div>
              )) : <p>No mini lessons found.</p>}
            </div>
          )}

          {activeTab === 'Conversations' && (
            <div>
              <p className="text-gray text-sm mb-4">Click "Inspect Tree" to view full branching structure (Feature coming in Phase 6).</p>
              {data?.scriptedConversations?.map((conv: any) => (
                <div key={conv.id} style={{ border: '1px solid #e2e8f0', padding: '15px', borderRadius: '6px', marginBottom: '15px' }}>
                  <h4 style={{ margin: '0 0 10px 0' }}>{conv.title} ({conv.id})</h4>
                  <p className="text-sm text-gray" style={{ margin: '0 0 10px 0' }}>{conv.messages?.length || 0} Turns</p>
                  <button className="admin-button-small" onClick={() => alert('Tree Inspector reserved for Phase 6 API updates')}>Inspect Tree</button>
                </div>
              ))}
            </div>
          )}
          
          {activeTab === 'Audits' && (
            <div>
              {certData ? (
                <div>
                  <h3 style={{ marginTop: 0 }}>Certification Data</h3>
                  <div style={{ backgroundColor: '#1e293b', color: '#f8fafc', padding: '15px', borderRadius: '6px', fontFamily: 'monospace', fontSize: '0.85rem', overflowX: 'auto' }}>
                    <pre style={{ margin: 0 }}>{JSON.stringify(certData, null, 2)}</pre>
                  </div>
                </div>
              ) : (
                <p>No certification data found for this scenario. Run the factory audit.</p>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

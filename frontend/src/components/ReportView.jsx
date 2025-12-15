import React, { useState, useEffect } from 'react'
import { getReport } from '../services/api'
import './ReportView.css'

function ReportView({ conversationId, onBack }) {
  const [report, setReport] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    loadReport()
  }, [conversationId])

  const loadReport = async () => {
    try {
      setLoading(true)
      const data = await getReport(conversationId)
      setReport(data)
      setError(null)
    } catch (err) {
      setError('Rapor yüklenirken hata oluştu: ' + err.message)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <div className="report-container">
        <div className="loading">Rapor hazırlanıyor...</div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="report-container">
        <div className="error">{error}</div>
        <button onClick={onBack} className="back-button">
          Senaryolara Dön
        </button>
      </div>
    )
  }

  if (!report) return null

  const getScoreColor = (score) => {
    if (score >= 85) return '#4caf50'
    if (score >= 70) return '#ff9800'
    return '#f44336'
  }

  return (
    <div className="report-container">
      <div className="report-header">
        <button className="back-button" onClick={onBack}>
          ← Senaryolara Dön
        </button>
        <h2>🎯 Gelişim Raporu</h2>
      </div>

      <div className="report-content">
        <section className="report-section overall-score">
          <h3>{report.scenario_title}</h3>
          <div className="score-circle" style={{ borderColor: getScoreColor(report.overall_score) }}>
            <span className="score-value">{report.overall_score.toFixed(1)}</span>
            <span className="score-label">Genel Puan</span>
          </div>
          <p className="summary">{report.summary}</p>
        </section>

        <section className="report-section competencies">
          <h3>Yetkinlik Değerlendirmeleri</h3>
          {report.competency_scores.map((comp) => (
            <div key={comp.competency_id} className="competency-card">
              <div className="competency-header">
                <h4>{comp.competency_name}</h4>
                <span
                  className="competency-score"
                  style={{ color: getScoreColor(comp.score) }}
                >
                  {comp.score.toFixed(1)}
                </span>
              </div>
              <div className="score-bar">
                <div
                  className="score-fill"
                  style={{
                    width: `${comp.score}%`,
                    backgroundColor: getScoreColor(comp.score),
                  }}
                />
              </div>
              <p className="feedback">{comp.feedback}</p>
              
              <div className="strengths-improvements">
                <div className="strengths">
                  <strong>✅ Güçlü Yönler:</strong>
                  <ul>
                    {comp.strengths.map((strength, idx) => (
                      <li key={idx}>{strength}</li>
                    ))}
                  </ul>
                </div>
                <div className="improvements">
                  <strong>📈 Gelişim Alanları:</strong>
                  <ul>
                    {comp.areas_for_improvement.map((area, idx) => (
                      <li key={idx}>{area}</li>
                    ))}
                  </ul>
                </div>
              </div>
            </div>
          ))}
        </section>

        <section className="report-section recommendations">
          <h3>Öneriler</h3>
          <ul>
            {report.recommendations.map((rec, idx) => (
              <li key={idx}>{rec}</li>
            ))}
          </ul>
        </section>

        <section className="report-section next-steps">
          <h3>Sonraki Adımlar</h3>
          <ol>
            {report.next_steps.map((step, idx) => (
              <li key={idx}>{step}</li>
            ))}
          </ol>
        </section>
      </div>

      <div className="report-actions">
        <button onClick={onBack} className="primary-button">
          Yeni Senaryo Dene
        </button>
      </div>
    </div>
  )
}

export default ReportView

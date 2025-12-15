import React from 'react'
import './ScenarioList.css'

function ScenarioList({ scenarios, loading, error, onSelectScenario }) {
  if (loading) {
    return (
      <div className="scenario-list-container">
        <div className="loading">Senaryolar yükleniyor...</div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="scenario-list-container">
        <div className="error">{error}</div>
      </div>
    )
  }

  const getDifficultyLabel = (level) => {
    const labels = {
      beginner: 'Başlangıç',
      intermediate: 'Orta',
      advanced: 'İleri',
    }
    return labels[level] || level
  }

  const getDifficultyColor = (level) => {
    const colors = {
      beginner: '#4caf50',
      intermediate: '#ff9800',
      advanced: '#f44336',
    }
    return colors[level] || '#666'
  }

  return (
    <div className="scenario-list-container">
      <h2>Liderlik Senaryoları</h2>
      <p className="intro-text">
        Liderlik becerilerinizi geliştirmek için bir senaryo seçin ve
        karşılıklı konuşma simülasyonuna başlayın.
      </p>

      <div className="scenarios-grid">
        {scenarios.map((scenario) => (
          <div
            key={scenario.id}
            className="scenario-card"
            onClick={() => onSelectScenario(scenario)}
          >
            <div className="scenario-header">
              <h3>{scenario.title}</h3>
              <span
                className="difficulty-badge"
                style={{ backgroundColor: getDifficultyColor(scenario.difficulty_level) }}
              >
                {getDifficultyLabel(scenario.difficulty_level)}
              </span>
            </div>
            <p className="scenario-description">{scenario.description}</p>
            <div className="scenario-competencies">
              <strong>Yetkinlikler:</strong>
              <ul>
                {scenario.competencies.map((comp) => (
                  <li key={comp.id}>{comp.name}</li>
                ))}
              </ul>
            </div>
            <button className="start-button">Başla</button>
          </div>
        ))}
      </div>
    </div>
  )
}

export default ScenarioList

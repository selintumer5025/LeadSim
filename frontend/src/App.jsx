import React, { useState, useEffect } from 'react'
import ScenarioList from './components/ScenarioList'
import ConversationView from './components/ConversationView'
import ReportView from './components/ReportView'
import { getScenarios } from './services/api'
import './App.css'

function App() {
  const [scenarios, setScenarios] = useState([])
  const [currentView, setCurrentView] = useState('scenarios') // scenarios, conversation, report
  const [selectedScenario, setSelectedScenario] = useState(null)
  const [conversationId, setConversationId] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    loadScenarios()
  }, [])

  const loadScenarios = async () => {
    try {
      setLoading(true)
      const data = await getScenarios()
      setScenarios(data)
      setError(null)
    } catch (err) {
      setError('Senaryolar yüklenirken hata oluştu: ' + err.message)
    } finally {
      setLoading(false)
    }
  }

  const handleScenarioSelect = (scenario) => {
    setSelectedScenario(scenario)
    setCurrentView('conversation')
  }

  const handleConversationStart = (convId) => {
    setConversationId(convId)
  }

  const handleConversationComplete = () => {
    setCurrentView('report')
  }

  const handleBackToScenarios = () => {
    setCurrentView('scenarios')
    setSelectedScenario(null)
    setConversationId(null)
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>🎯 LeadSim</h1>
        <p className="subtitle">Liderlik Gelişim Portalı</p>
      </header>

      <main className="app-main">
        {currentView === 'scenarios' && (
          <ScenarioList
            scenarios={scenarios}
            loading={loading}
            error={error}
            onSelectScenario={handleScenarioSelect}
          />
        )}

        {currentView === 'conversation' && selectedScenario && (
          <ConversationView
            scenario={selectedScenario}
            onConversationStart={handleConversationStart}
            onComplete={handleConversationComplete}
            onBack={handleBackToScenarios}
          />
        )}

        {currentView === 'report' && conversationId && (
          <ReportView
            conversationId={conversationId}
            onBack={handleBackToScenarios}
          />
        )}
      </main>

      <footer className="app-footer">
        <p>© 2024 LeadSim - Liderlik Gelişim Sistemi</p>
      </footer>
    </div>
  )
}

export default App

import React, { useState, useEffect, useRef } from 'react'
import { startConversation, sendMessage } from '../services/api'
import './ConversationView.css'

function ConversationView({ scenario, onConversationStart, onComplete, onBack }) {
  const [conversationId, setConversationId] = useState(null)
  const [messages, setMessages] = useState([])
  const [inputMessage, setInputMessage] = useState('')
  const [loading, setLoading] = useState(false)
  const [isComplete, setIsComplete] = useState(false)
  const messagesEndRef = useRef(null)

  useEffect(() => {
    initializeConversation()
  }, [])

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  const initializeConversation = async () => {
    try {
      setLoading(true)
      const response = await startConversation(scenario.id)
      setConversationId(response.conversation_id)
      onConversationStart(response.conversation_id)
      
      setMessages([
        {
          role: 'assistant',
          content: response.initial_message,
          timestamp: new Date().toISOString(),
        },
      ])
    } catch (error) {
      console.error('Konuşma başlatılırken hata:', error)
      alert('Konuşma başlatılırken hata oluştu')
    } finally {
      setLoading(false)
    }
  }

  const handleSendMessage = async (e) => {
    e.preventDefault()
    if (!inputMessage.trim() || !conversationId || loading) return

    const userMessage = {
      role: 'user',
      content: inputMessage,
      timestamp: new Date().toISOString(),
    }

    setMessages((prev) => [...prev, userMessage])
    setInputMessage('')
    setLoading(true)

    try {
      const response = await sendMessage(conversationId, inputMessage)
      
      const assistantMessage = {
        role: 'assistant',
        content: response.message,
        timestamp: new Date().toISOString(),
      }

      setMessages((prev) => [...prev, assistantMessage])

      if (response.is_complete) {
        setIsComplete(true)
      }
    } catch (error) {
      console.error('Mesaj gönderilirken hata:', error)
      alert('Mesaj gönderilirken hata oluştu')
    } finally {
      setLoading(false)
    }
  }

  const handleViewReport = () => {
    onComplete()
  }

  return (
    <div className="conversation-container">
      <div className="conversation-header">
        <button className="back-button" onClick={onBack}>
          ← Geri
        </button>
        <div>
          <h2>{scenario.title}</h2>
          <p className="scenario-context">{scenario.context}</p>
        </div>
      </div>

      <div className="messages-container">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`message ${message.role === 'user' ? 'user-message' : 'assistant-message'}`}
          >
            <div className="message-content">{message.content}</div>
            <div className="message-time">
              {new Date(message.timestamp).toLocaleTimeString('tr-TR')}
            </div>
          </div>
        ))}
        {loading && (
          <div className="message assistant-message">
            <div className="message-content typing-indicator">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {!isComplete ? (
        <form className="input-form" onSubmit={handleSendMessage}>
          <input
            type="text"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            placeholder="Yanıtınızı yazın..."
            disabled={loading}
            className="message-input"
          />
          <button type="submit" disabled={loading || !inputMessage.trim()} className="send-button">
            Gönder
          </button>
        </form>
      ) : (
        <div className="completion-message">
          <p>✅ Konuşma tamamlandı!</p>
          <button onClick={handleViewReport} className="report-button">
            Gelişim Raporunu Görüntüle
          </button>
        </div>
      )}
    </div>
  )
}

export default ConversationView

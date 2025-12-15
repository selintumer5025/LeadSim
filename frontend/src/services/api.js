import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const getScenarios = async () => {
  const response = await api.get('/scenarios/')
  return response.data
}

export const getScenario = async (scenarioId) => {
  const response = await api.get(`/scenarios/${scenarioId}`)
  return response.data
}

export const startConversation = async (scenarioId) => {
  const response = await api.post('/conversations/start', {
    scenario_id: scenarioId,
  })
  return response.data
}

export const sendMessage = async (conversationId, message) => {
  const response = await api.post(`/conversations/${conversationId}/message`, {
    message,
  })
  return response.data
}

export const getReport = async (conversationId) => {
  const response = await api.get(`/reports/${conversationId}`)
  return response.data
}

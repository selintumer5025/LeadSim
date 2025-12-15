# LeadSim - Liderlik Gelişim Portalı

Leadership Development Portal - A comprehensive platform for developing leadership skills through interactive scenario-based simulations.

## 🎯 Overview

LeadSim is a leadership development platform that provides:
- **Scenario-based learning**: Interactive leadership scenarios covering various competencies
- **Conversational simulations**: Engage in realistic leadership conversations
- **Development reports**: Detailed feedback on competencies and areas for improvement
- **Separated architecture**: Independent frontend and backend services

## 🏗️ Architecture

The project consists of two separate applications:

### Backend (FastAPI)
- **Framework**: FastAPI (Python)
- **Features**: REST API, scenario management, conversation handling, report generation
- **Port**: 8000

### Frontend (React)
- **Framework**: React 18 with Vite
- **Features**: Interactive UI, scenario selection, conversation interface, report viewing
- **Port**: 3000

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 18+
- npm or yarn

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the backend server:
```bash
python run.py
```

The backend API will be available at http://localhost:8000
API documentation at http://localhost:8000/docs

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at http://localhost:3000

## 📁 Project Structure

```
LeadSim/
├── backend/                 # Backend API (FastAPI)
│   ├── app/
│   │   ├── models/         # Data models
│   │   ├── routes/         # API endpoints
│   │   ├── services/       # Business logic
│   │   └── main.py         # FastAPI application
│   ├── data/
│   │   └── scenarios.json  # Scenario definitions
│   ├── requirements.txt    # Python dependencies
│   └── run.py             # Server startup script
│
├── frontend/               # Frontend app (React)
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── services/      # API client
│   │   ├── App.jsx        # Main app component
│   │   └── main.jsx       # Entry point
│   ├── package.json       # Node dependencies
│   └── vite.config.js     # Vite configuration
│
└── README.md              # This file
```

## 🎓 Features

### 1. Scenario Selection
- Browse available leadership scenarios
- Filter by difficulty level (Beginner, Intermediate, Advanced)
- View competencies covered in each scenario

### 2. Interactive Conversations
- Engage in realistic leadership dialogues
- Receive contextual responses based on your inputs
- Progress through multiple conversation turns

### 3. Development Reports
- Detailed competency assessments
- Overall performance score
- Strengths and areas for improvement
- Personalized recommendations
- Actionable next steps

## 🛠️ Development

### Adding New Scenarios

Edit `backend/data/scenarios.json` to add new leadership scenarios. Each scenario should include:
- Unique ID
- Title and description (in Turkish)
- Context and initial prompt
- List of competencies to assess
- Difficulty level

### Customizing Competencies

Scenarios can assess various leadership competencies such as:
- Communication (İletişim)
- Conflict Management (Çatışma Yönetimi)
- Emotional Intelligence (Duygusal Zeka)
- Change Leadership (Değişim Liderliği)
- Delegation (Yetki Devri)
- Team Development (Ekip Gelişimi)

## 🔗 API Endpoints

### Scenarios
- `GET /api/scenarios/` - List all scenarios
- `GET /api/scenarios/{id}` - Get scenario details

### Conversations
- `POST /api/conversations/start` - Start new conversation
- `POST /api/conversations/{id}/message` - Send message

### Reports
- `GET /api/reports/{conversation_id}` - Get development report

## 📝 License

See LICENSE file for details.

## 🤝 Contributing

This is a leadership development platform designed to help current and aspiring leaders develop their skills through interactive simulations.

## 📧 Contact

For questions or support, please open an issue in the repository.

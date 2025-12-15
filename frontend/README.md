# LeadSim Frontend

Leadership Development Portal Frontend Application

## Tech Stack

- **React 18**: Modern React with hooks
- **Vite**: Fast build tool and dev server
- **Axios**: HTTP client for API calls
- **CSS3**: Modern styling with flexbox and grid

## Setup

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

The application will be available at http://localhost:3000

3. Build for production:
```bash
npm run build
```

## Features

- **Scenario Selection**: Browse and select leadership scenarios
- **Interactive Conversations**: Engage in simulated leadership conversations
- **Development Reports**: View detailed feedback and competency assessments
- **Responsive Design**: Works on desktop and mobile devices

## Project Structure

```
frontend/
├── src/
│   ├── components/       # React components
│   │   ├── ScenarioList.jsx
│   │   ├── ConversationView.jsx
│   │   └── ReportView.jsx
│   ├── services/         # API service layer
│   │   └── api.js
│   ├── App.jsx           # Main application component
│   ├── main.jsx          # Application entry point
│   └── index.css         # Global styles
├── public/               # Static assets
├── index.html            # HTML template
├── vite.config.js        # Vite configuration
└── package.json          # Dependencies
```

## API Integration

The frontend communicates with the backend API running on `http://localhost:8000`. The API endpoints are:

- `GET /api/scenarios/` - Get all scenarios
- `POST /api/conversations/start` - Start a conversation
- `POST /api/conversations/{id}/message` - Send a message
- `GET /api/reports/{id}` - Get development report

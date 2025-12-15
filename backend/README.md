# LeadSim Backend

Leadership Development Portal Backend API

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python run.py
```

Or using uvicorn directly:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Scenarios
- `GET /api/scenarios/` - Get all scenarios
- `GET /api/scenarios/{scenario_id}` - Get specific scenario

### Conversations
- `POST /api/conversations/start` - Start a new conversation
- `POST /api/conversations/{conversation_id}/message` - Send a message

### Reports
- `GET /api/reports/{conversation_id}` - Get development report

## Architecture

- **FastAPI**: Modern, fast web framework
- **Pydantic**: Data validation
- **Service Layer**: Business logic separation
- **Models**: Data structures for scenarios, conversations, and reports

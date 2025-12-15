# LeadSim Architecture Documentation

## Overview

LeadSim is a leadership development portal built with a separated frontend-backend architecture. This document explains key architectural decisions and limitations.

## Backend Architecture

### Service Layer Pattern

The backend uses a service layer pattern with three main services:

1. **ScenarioService**: Manages leadership scenarios
2. **ConversationService**: Handles conversation state
3. **ReportService**: Generates development reports

### Dependency Injection

Services are instantiated as singletons in `app/dependencies.py`. This is appropriate for the current single-user development/demo environment.

**Production Considerations:**
- For multi-user production environments, consider:
  - Using FastAPI's dependency injection system with `Depends()`
  - Implementing database-backed storage instead of in-memory state
  - Adding user authentication and session management
  - Using Redis or similar for distributed state management

### Conversation Management

**Current Implementation:**
- Conversations are stored in memory in the ConversationService
- Simple threshold-based completion (10 messages)
- State is shared across all service instances

**Production Recommendations:**
- Store conversations in a database (PostgreSQL, MongoDB)
- Make conversation length configurable per scenario
- Implement timeout-based conversation cleanup
- Add user-specific conversation isolation

### Scoring Algorithm

**Current Implementation:**
The report generation uses a deterministic scoring algorithm based on:
- Message count (engagement level)
- Competency weights
- Consistent calculation for reproducibility

**Limitations:**
This is a placeholder implementation suitable for demonstration. It does NOT analyze actual conversation content.

**Production Recommendations:**
- Implement NLP/AI-based content analysis
- Use pre-trained language models for competency assessment
- Analyze response quality, not just quantity
- Consider integrating services like:
  - OpenAI GPT for conversation analysis
  - Custom fine-tuned models for leadership competencies
  - Sentiment analysis for emotional intelligence assessment

## Frontend Architecture

### Component Structure

```
src/
├── components/
│   ├── ScenarioList.jsx    - Browse scenarios
│   ├── ConversationView.jsx - Chat interface
│   └── ReportView.jsx       - Development report
├── services/
│   └── api.js               - Backend API client
└── App.jsx                  - Main application
```

### State Management

Currently uses React's built-in state management (useState, useEffect).

**Production Considerations:**
- For complex state needs, consider Redux or Zustand
- Implement proper error boundaries
- Add loading states and retry logic
- Cache API responses appropriately

### Environment Configuration

**Current Setup:**
- `VITE_API_BASE_URL` for API endpoint configuration
- Development defaults to localhost

**Production Recommendations:**
- Use separate .env files for dev/staging/production
- Implement environment-specific builds
- Consider using a backend URL without hardcoded '/api' path

## Data Storage

### Current Approach

- **Scenarios**: JSON files (`backend/data/scenarios.json`)
- **Conversations**: In-memory storage
- **Reports**: Generated on-demand, not persisted

### Production Approach

**Database Schema Recommendations:**

```
users
  - id, username, email, created_at

scenarios
  - id, title, description, context, difficulty_level

competencies
  - id, name, description, weight

scenario_competencies
  - scenario_id, competency_id

conversations
  - id, user_id, scenario_id, started_at, completed_at

messages
  - id, conversation_id, role, content, timestamp

reports
  - id, conversation_id, user_id, overall_score, generated_at

competency_scores
  - id, report_id, competency_id, score, feedback
```

## Security Considerations

### Current Security Posture

- CORS configured for localhost development
- No authentication or authorization
- No input validation beyond Pydantic models
- No rate limiting

### Production Security Requirements

1. **Authentication & Authorization**
   - Implement JWT-based authentication
   - Role-based access control (admin, user)
   - Secure session management

2. **Input Validation**
   - Comprehensive input sanitization
   - SQL injection prevention (use ORMs)
   - XSS protection
   - Rate limiting on API endpoints

3. **Data Protection**
   - HTTPS only in production
   - Encrypt sensitive data at rest
   - Implement proper CORS policies
   - Add CSRF protection

4. **API Security**
   - API key or OAuth for third-party integrations
   - Request throttling
   - Audit logging

## Scalability Considerations

### Current Limitations

- Single-instance deployment
- In-memory state storage
- No caching layer
- Synchronous processing

### Scaling Recommendations

1. **Horizontal Scaling**
   - Stateless API servers behind load balancer
   - Shared database for all instances
   - Redis for distributed caching

2. **Performance Optimization**
   - Implement caching (Redis)
   - Use CDN for static assets
   - Optimize database queries
   - Consider async processing for reports

3. **Monitoring & Observability**
   - Application performance monitoring (APM)
   - Logging infrastructure (ELK stack)
   - Error tracking (Sentry)
   - Metrics and dashboards

## Deployment

### Development
```bash
# Backend
cd backend && python run.py

# Frontend
cd frontend && npm run dev
```

### Production Deployment Options

1. **Docker Containers**
   ```dockerfile
   # Backend: Python container with Gunicorn/Uvicorn
   # Frontend: Nginx serving static build
   ```

2. **Cloud Platforms**
   - Backend: AWS ECS, Google Cloud Run, Azure Container Instances
   - Frontend: Vercel, Netlify, AWS S3 + CloudFront
   - Database: AWS RDS, Google Cloud SQL, Azure Database

3. **Platform as a Service**
   - Heroku, Railway, Render
   - Automated deployments from Git

## Testing Strategy

### Current Testing

Manual testing of:
- API endpoints
- UI components
- End-to-end flow

### Production Testing Recommendations

1. **Backend Testing**
   - Unit tests (pytest)
   - Integration tests
   - API contract tests
   - Load testing

2. **Frontend Testing**
   - Component tests (React Testing Library)
   - Integration tests
   - E2E tests (Playwright, Cypress)
   - Visual regression tests

3. **CI/CD Pipeline**
   - Automated test runs
   - Code quality checks (linting, type checking)
   - Security scanning
   - Automated deployments

## Conclusion

This architecture is suitable for:
- ✅ Development and demonstration
- ✅ Small-scale deployments (single user)
- ✅ Proof of concept

For production use with multiple users, implement:
- 🔧 Database-backed storage
- 🔧 User authentication
- 🔧 AI/NLP-based scoring
- 🔧 Comprehensive security measures
- 🔧 Monitoring and logging
- 🔧 Scalable infrastructure

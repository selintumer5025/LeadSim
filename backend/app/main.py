from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import scenarios, conversations, reports

app = FastAPI(
    title="LeadSim API",
    description="Leadership Development Portal API",
    version="1.0.0"
)

# Configure CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(scenarios.router)
app.include_router(conversations.router)
app.include_router(reports.router)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to LeadSim API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}

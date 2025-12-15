from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models import ConversationResponse
from app.dependencies import conversation_service, scenario_service

router = APIRouter(prefix="/api/conversations", tags=["conversations"])


class StartConversationRequest(BaseModel):
    scenario_id: str


class StartConversationResponse(BaseModel):
    conversation_id: str
    initial_message: str


class SendMessageRequest(BaseModel):
    message: str


@router.post("/start", response_model=StartConversationResponse)
async def start_conversation(request: StartConversationRequest):
    """Start a new conversation for a scenario"""
    scenario = scenario_service.get_scenario_by_id(request.scenario_id)
    if not scenario:
        raise HTTPException(status_code=404, detail="Scenario not found")
    
    conversation_id, initial_prompt = conversation_service.start_conversation(scenario)
    
    return StartConversationResponse(
        conversation_id=conversation_id,
        initial_message=initial_prompt
    )


@router.post("/{conversation_id}/message", response_model=ConversationResponse)
async def send_message(conversation_id: str, request: SendMessageRequest):
    """Send a message in an ongoing conversation"""
    try:
        conversation = conversation_service.get_conversation(conversation_id)
        scenario = scenario_service.get_scenario_by_id(conversation.scenario_id)
        
        if not scenario:
            raise HTTPException(status_code=404, detail="Scenario not found")
        
        response = conversation_service.process_message(
            conversation_id,
            request.message,
            scenario
        )
        
        return response
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

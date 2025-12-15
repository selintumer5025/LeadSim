from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Message(BaseModel):
    """Represents a single message in the conversation"""
    role: str  # "user" or "assistant"
    content: str
    timestamp: Optional[str] = None


class Conversation(BaseModel):
    """Represents an ongoing conversation"""
    scenario_id: str
    messages: List[Message]


class ConversationResponse(BaseModel):
    """Response to a conversation message"""
    message: str
    is_complete: bool = False
    next_prompt: Optional[str] = None

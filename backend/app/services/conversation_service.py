from typing import Dict, List, Tuple
from app.models import Message, Conversation, ConversationResponse, Scenario
from datetime import datetime


class ConversationService:
    """Service for managing conversations"""
    
    def __init__(self):
        self.conversations: Dict[str, Conversation] = {}
        self.conversation_counter = 0
    
    def start_conversation(self, scenario: Scenario) -> Tuple[str, str]:
        """Start a new conversation for a scenario"""
        conversation_id = f"conv_{self.conversation_counter}"
        self.conversation_counter += 1
        
        self.conversations[conversation_id] = Conversation(
            scenario_id=scenario.id,
            messages=[]
        )
        
        return conversation_id, scenario.initial_prompt
    
    def process_message(
        self, 
        conversation_id: str, 
        user_message: str, 
        scenario: Scenario
    ) -> ConversationResponse:
        """Process a user message and generate a response"""
        if conversation_id not in self.conversations:
            raise ValueError(f"Conversation {conversation_id} not found")
        
        conversation = self.conversations[conversation_id]
        
        # Add user message
        conversation.messages.append(Message(
            role="user",
            content=user_message,
            timestamp=datetime.now().isoformat()
        ))
        
        # Generate response based on scenario and conversation history
        response_text = self._generate_response(conversation, scenario)
        
        # Add assistant message
        conversation.messages.append(Message(
            role="assistant",
            content=response_text,
            timestamp=datetime.now().isoformat()
        ))
        
        # Check if conversation should end (simple heuristic: after 5 exchanges)
        is_complete = len(conversation.messages) >= 10
        
        return ConversationResponse(
            message=response_text,
            is_complete=is_complete,
            next_prompt="Please continue the conversation..." if not is_complete else None
        )
    
    def _generate_response(self, conversation: Conversation, scenario: Scenario) -> str:
        """Generate a response based on the scenario and conversation context"""
        # This is a simplified version. In production, this would use AI/LLM
        message_count = len(conversation.messages)
        
        responses = [
            f"Thank you for your response. In the context of {scenario.title}, how would you handle the situation if stakeholders disagreed?",
            "That's an interesting approach. Can you elaborate on how you would prioritize competing demands?",
            "I see your point. How would you ensure team alignment while making this decision?",
            "Good thinking. What metrics would you use to measure success in this scenario?",
            "Excellent. As a final question, what would you do differently if you could start over?"
        ]
        
        if message_count < len(responses):
            return responses[message_count]
        else:
            return "Thank you for your thoughtful responses. The conversation is now complete."
    
    def get_conversation(self, conversation_id: str) -> Conversation:
        """Get a conversation by ID"""
        if conversation_id not in self.conversations:
            raise ValueError(f"Conversation {conversation_id} not found")
        return self.conversations[conversation_id]

from fastapi import APIRouter, HTTPException
from app.services.conversation_service import ConversationService
from app.services.scenario_service import ScenarioService
from app.services.report_service import ReportService
from app.models import DevelopmentReport

router = APIRouter(prefix="/api/reports", tags=["reports"])
conversation_service = ConversationService()
scenario_service = ScenarioService()
report_service = ReportService()


@router.get("/{conversation_id}", response_model=DevelopmentReport)
async def get_report(conversation_id: str):
    """Generate and retrieve development report for a conversation"""
    try:
        conversation = conversation_service.get_conversation(conversation_id)
        scenario = scenario_service.get_scenario_by_id(conversation.scenario_id)
        
        if not scenario:
            raise HTTPException(status_code=404, detail="Scenario not found")
        
        report = report_service.generate_report(conversation, scenario)
        return report
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

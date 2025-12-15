"""Shared service instances for dependency injection"""
from app.services.scenario_service import ScenarioService
from app.services.conversation_service import ConversationService
from app.services.report_service import ReportService

# Create singleton service instances
scenario_service = ScenarioService()
conversation_service = ConversationService()
report_service = ReportService()

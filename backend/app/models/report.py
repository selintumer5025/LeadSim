from pydantic import BaseModel
from typing import List, Dict, Optional


class CompetencyScore(BaseModel):
    """Score for a specific competency"""
    competency_id: str
    competency_name: str
    score: float  # 0-100
    feedback: str
    strengths: List[str]
    areas_for_improvement: List[str]


class DevelopmentReport(BaseModel):
    """Complete development report for a conversation"""
    scenario_id: str
    scenario_title: str
    overall_score: float  # 0-100
    competency_scores: List[CompetencyScore]
    summary: str
    recommendations: List[str]
    next_steps: List[str]

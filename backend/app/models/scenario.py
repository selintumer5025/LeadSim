from pydantic import BaseModel
from typing import List, Optional


class Competency(BaseModel):
    """Represents a leadership competency to be assessed"""
    id: str
    name: str
    description: str
    weight: float = 1.0


class Scenario(BaseModel):
    """Represents a leadership scenario for simulation"""
    id: str
    title: str
    description: str
    context: str
    competencies: List[Competency]
    initial_prompt: str
    difficulty_level: str = "intermediate"

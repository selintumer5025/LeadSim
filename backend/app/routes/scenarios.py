from fastapi import APIRouter, HTTPException
from app.models import Scenario
from typing import List
from app.dependencies import scenario_service

router = APIRouter(prefix="/api/scenarios", tags=["scenarios"])


@router.get("/", response_model=List[Scenario])
async def get_scenarios():
    """Get all available leadership scenarios"""
    return scenario_service.get_all_scenarios()


@router.get("/{scenario_id}", response_model=Scenario)
async def get_scenario(scenario_id: str):
    """Get a specific scenario by ID"""
    scenario = scenario_service.get_scenario_by_id(scenario_id)
    if not scenario:
        raise HTTPException(status_code=404, detail="Scenario not found")
    return scenario

import json
import os
from typing import List, Optional
from app.models import Scenario


class ScenarioService:
    """Service for managing leadership scenarios"""
    
    def __init__(self, data_path: str = "data/scenarios.json"):
        self.data_path = data_path
        self.scenarios = self._load_scenarios()
    
    def _load_scenarios(self) -> List[Scenario]:
        """Load scenarios from JSON file"""
        if os.path.exists(self.data_path):
            with open(self.data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Scenario(**scenario) for scenario in data]
        return []
    
    def get_all_scenarios(self) -> List[Scenario]:
        """Get all available scenarios"""
        return self.scenarios
    
    def get_scenario_by_id(self, scenario_id: str) -> Optional[Scenario]:
        """Get a specific scenario by ID"""
        for scenario in self.scenarios:
            if scenario.id == scenario_id:
                return scenario
        return None

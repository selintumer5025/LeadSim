from app.models import (
    Conversation, 
    Scenario, 
    DevelopmentReport, 
    CompetencyScore
)
from typing import List


class ReportService:
    """Service for generating development reports"""
    
    def generate_report(
        self, 
        conversation: Conversation, 
        scenario: Scenario
    ) -> DevelopmentReport:
        """Generate a development report based on the conversation"""
        
        # Analyze conversation and generate scores for each competency
        competency_scores = self._analyze_competencies(
            conversation, 
            scenario
        )
        
        # Calculate overall score
        overall_score = sum(cs.score for cs in competency_scores) / len(competency_scores)
        
        # Generate summary and recommendations
        summary = self._generate_summary(overall_score, scenario)
        recommendations = self._generate_recommendations(competency_scores)
        next_steps = self._generate_next_steps(competency_scores)
        
        return DevelopmentReport(
            scenario_id=scenario.id,
            scenario_title=scenario.title,
            overall_score=round(overall_score, 2),
            competency_scores=competency_scores,
            summary=summary,
            recommendations=recommendations,
            next_steps=next_steps
        )
    
    def _analyze_competencies(
        self, 
        conversation: Conversation, 
        scenario: Scenario
    ) -> List[CompetencyScore]:
        """Analyze conversation and score each competency
        
        Note: This is a simplified implementation for demonstration.
        In production, this should use NLP/AI analysis to evaluate responses
        based on actual conversation content and competency indicators.
        """
        scores = []
        
        for competency in scenario.competencies:
            # Simplified scoring - uses conversation engagement as a proxy
            # TODO: Replace with actual NLP/AI-based content analysis
            message_count = len([m for m in conversation.messages if m.role == "user"])
            
            # Base score from engagement (more messages = more engagement)
            engagement_score = min(60 + (message_count * 5), 85)
            
            # Add variance based on competency weight and conversation length
            # Using deterministic approach based on message count for consistency
            weight_bonus = competency.weight * (message_count % 10)
            
            final_score = min(engagement_score + weight_bonus, 100)
            
            scores.append(CompetencyScore(
                competency_id=competency.id,
                competency_name=competency.name,
                score=round(final_score, 2),
                feedback=self._generate_feedback(competency, final_score),
                strengths=self._identify_strengths(competency, final_score),
                areas_for_improvement=self._identify_improvements(competency, final_score)
            ))
        
        return scores
    
    def _generate_feedback(self, competency, score: float) -> str:
        """Generate feedback for a competency"""
        if score >= 85:
            return f"Excellent demonstration of {competency.name}. Your responses showed strong understanding and application."
        elif score >= 70:
            return f"Good grasp of {competency.name}. Your approach was solid with room for refinement."
        else:
            return f"Developing skills in {competency.name}. Continue practicing to strengthen this competency."
    
    def _identify_strengths(self, competency, score: float) -> List[str]:
        """Identify strengths in a competency"""
        strengths = [
            f"Clear understanding of {competency.name} principles",
            "Thoughtful consideration of multiple perspectives",
            "Practical approach to problem-solving"
        ]
        return strengths[:2] if score >= 75 else strengths[:1]
    
    def _identify_improvements(self, competency, score: float) -> List[str]:
        """Identify areas for improvement"""
        improvements = [
            f"Consider more diverse scenarios for {competency.name}",
            "Practice articulating rationale more explicitly",
            "Explore alternative approaches to complex situations"
        ]
        return improvements[:1] if score >= 75 else improvements[:2]
    
    def _generate_summary(self, overall_score: float, scenario: Scenario) -> str:
        """Generate overall summary"""
        if overall_score >= 85:
            level = "advanced"
            message = "exceptional leadership capabilities"
        elif overall_score >= 70:
            level = "proficient"
            message = "solid leadership skills"
        else:
            level = "developing"
            message = "emerging leadership potential"
        
        return (
            f"Your performance in the '{scenario.title}' scenario demonstrates {message}. "
            f"You are at a {level} level with an overall score of {overall_score:.1f}%. "
            f"Continue building on your strengths while focusing on identified growth areas."
        )
    
    def _generate_recommendations(self, scores: List[CompetencyScore]) -> List[str]:
        """Generate personalized recommendations"""
        recommendations = [
            "Practice leadership scenarios regularly to build confidence",
            "Seek feedback from peers and mentors on leadership style",
            "Read case studies on effective leadership in similar contexts"
        ]
        
        # Add specific recommendations based on lowest scores
        lowest_score = min(scores, key=lambda x: x.score)
        if lowest_score.score < 75:
            recommendations.insert(
                0, 
                f"Focus on developing {lowest_score.competency_name} through targeted practice"
            )
        
        return recommendations
    
    def _generate_next_steps(self, scores: List[CompetencyScore]) -> List[str]:
        """Generate actionable next steps"""
        return [
            "Complete additional scenarios to practice different competencies",
            "Review the feedback and identify 2-3 specific areas to work on",
            "Schedule a follow-up assessment in 30 days to track progress",
            "Apply learned techniques in real leadership situations"
        ]

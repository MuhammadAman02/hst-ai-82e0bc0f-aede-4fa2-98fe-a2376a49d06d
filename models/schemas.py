"""Pydantic models for data validation"""

from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional, List

class UserGreeting(BaseModel):
    """Model for user greeting data"""
    name: str = Field(..., min_length=1, max_length=100, description="User's name")
    timestamp: datetime = Field(default_factory=datetime.now)
    greeting_count: int = Field(default=1, ge=1)
    
    @validator('name')
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()

class GreetingResponse(BaseModel):
    """Model for greeting response"""
    message: str
    personalized: bool = False
    fun_fact: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)

class AppStatus(BaseModel):
    """Model for application health status"""
    status: str = "healthy"
    timestamp: datetime = Field(default_factory=datetime.now)
    version: str = "1.0.0"
    uptime_seconds: Optional[float] = None

class ProjectIdea(BaseModel):
    """Model for project ideas"""
    title: str
    description: str
    icon: str
    difficulty: str = Field(..., regex="^(Beginner|Intermediate|Advanced)$")
    estimated_time: str
    technologies: List[str] = []
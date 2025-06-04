"""Business logic for greeting functionality"""

import random
from datetime import datetime
from typing import List, Dict
from models.schemas import UserGreeting, GreetingResponse, ProjectIdea

class GreetingService:
    """Service class for handling greeting logic"""
    
    def __init__(self):
        self.greetings = [
            "Hello there! 👋",
            "Welcome! 🎉", 
            "Greetings! 🌟",
            "Hi! Nice to meet you! 😊",
            "Hello and welcome! 🚀",
            "Hey there! 👋✨"
        ]
        
        self.fun_facts = [
            "🤖 I can build full-stack Python applications in minutes!",
            "⚡ I use NiceGUI for rapid, beautiful UI development",
            "🎨 I automatically select professional color schemes and images",
            "🔧 I follow enterprise-grade architecture patterns",
            "🚀 I create production-ready, deployable applications",
            "💡 I can integrate databases, APIs, and authentication seamlessly"
        ]
        
        self.project_ideas = [
            ProjectIdea(
                title="Interactive Dashboard",
                description="Real-time data visualization with charts and metrics",
                icon="📊",
                difficulty="Intermediate",
                estimated_time="2-3 hours",
                technologies=["NiceGUI", "Plotly", "Pandas"]
            ),
            ProjectIdea(
                title="E-commerce Platform",
                description="Full-featured online store with payment integration",
                icon="🛒",
                difficulty="Advanced", 
                estimated_time="1-2 days",
                technologies=["FastAPI", "SQLAlchemy", "Stripe"]
            ),
            ProjectIdea(
                title="AI Chatbot",
                description="Intelligent conversational interface",
                icon="🤖",
                difficulty="Advanced",
                estimated_time="4-6 hours",
                technologies=["NiceGUI", "OpenAI", "LangChain"]
            )
        ]
    
    def get_random_greeting(self) -> str:
        """Get a random greeting message"""
        return random.choice(self.greetings)
    
    def get_random_fun_fact(self) -> str:
        """Get a random fun fact"""
        return random.choice(self.fun_facts)
    
    def create_personalized_greeting(self, user_greeting: UserGreeting) -> GreetingResponse:
        """Create a personalized greeting response"""
        base_message = f"Hello, {user_greeting.name}! 🎉"
        
        if user_greeting.greeting_count > 1:
            base_message += f" Welcome back for the {self._ordinal(user_greeting.greeting_count)} time!"
        
        return GreetingResponse(
            message=base_message,
            personalized=True,
            fun_fact=self.get_random_fun_fact(),
            timestamp=datetime.now()
        )
    
    def get_project_ideas(self) -> List[ProjectIdea]:
        """Get list of project ideas"""
        return self.project_ideas
    
    def _ordinal(self, n: int) -> str:
        """Convert number to ordinal (1st, 2nd, 3rd, etc.)"""
        if 10 <= n % 100 <= 20:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
        return f"{n}{suffix}"
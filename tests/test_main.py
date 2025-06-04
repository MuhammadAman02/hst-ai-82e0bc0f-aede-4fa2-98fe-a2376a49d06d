"""Tests for the main application functionality"""

import pytest
from unittest.mock import Mock, patch
from models.schemas import UserGreeting, GreetingResponse
from services.greeting_service import GreetingService
from core.utils import validate_user_input, format_greeting_count

class TestGreetingService:
    """Test cases for GreetingService"""
    
    def setup_method(self):
        self.service = GreetingService()
    
    def test_get_random_greeting(self):
        """Test random greeting generation"""
        greeting = self.service.get_random_greeting()
        assert isinstance(greeting, str)
        assert len(greeting) > 0
        assert greeting in self.service.greetings
    
    def test_get_random_fun_fact(self):
        """Test random fun fact generation"""
        fact = self.service.get_random_fun_fact()
        assert isinstance(fact, str)
        assert len(fact) > 0
        assert fact in self.service.fun_facts
    
    def test_create_personalized_greeting(self):
        """Test personalized greeting creation"""
        user_greeting = UserGreeting(name="Alice", greeting_count=1)
        response = self.service.create_personalized_greeting(user_greeting)
        
        assert isinstance(response, GreetingResponse)
        assert "Alice" in response.message
        assert response.personalized is True
        assert response.fun_fact is not None

class TestUtils:
    """Test cases for utility functions"""
    
    def test_validate_user_input_valid(self):
        """Test valid user input validation"""
        result = validate_user_input("Alice")
        assert result["is_valid"] is True
        assert result["cleaned_text"] == "Alice"
        assert len(result["errors"]) == 0
    
    def test_validate_user_input_empty(self):
        """Test empty user input validation"""
        result = validate_user_input("")
        assert result["is_valid"] is False
        assert len(result["errors"]) > 0
    
    def test_validate_user_input_too_long(self):
        """Test too long user input validation"""
        long_input = "a" * 101
        result = validate_user_input(long_input)
        assert result["is_valid"] is False
        assert len(result["errors"]) > 0
    
    def test_format_greeting_count(self):
        """Test greeting count formatting"""
        assert format_greeting_count(1) == "1st"
        assert format_greeting_count(2) == "2nd"
        assert format_greeting_count(3) == "3rd"
        assert format_greeting_count(4) == "4th"
        assert format_greeting_count(11) == "11th"
        assert format_greeting_count(21) == "21st"

class TestModels:
    """Test cases for Pydantic models"""
    
    def test_user_greeting_valid(self):
        """Test valid UserGreeting model"""
        greeting = UserGreeting(name="Bob", greeting_count=5)
        assert greeting.name == "Bob"
        assert greeting.greeting_count == 5
        assert greeting.timestamp is not None
    
    def test_user_greeting_invalid_name(self):
        """Test invalid UserGreeting with empty name"""
        with pytest.raises(ValueError):
            UserGreeting(name="", greeting_count=1)
    
    def test_greeting_response_creation(self):
        """Test GreetingResponse model creation"""
        response = GreetingResponse(
            message="Hello!",
            personalized=True,
            fun_fact="Test fact"
        )
        assert response.message == "Hello!"
        assert response.personalized is True
        assert response.fun_fact == "Test fact"
        assert response.timestamp is not None
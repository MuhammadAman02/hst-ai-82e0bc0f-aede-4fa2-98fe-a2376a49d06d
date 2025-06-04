"""Pytest configuration and fixtures"""

import pytest
from unittest.mock import Mock
from services.greeting_service import GreetingService

@pytest.fixture
def greeting_service():
    """Fixture for GreetingService instance"""
    return GreetingService()

@pytest.fixture
def mock_user_input():
    """Fixture for mock user input"""
    return {
        "valid_name": "Alice",
        "empty_name": "",
        "long_name": "a" * 101,
        "special_chars": "Alice@123"
    }

@pytest.fixture
def sample_greeting_data():
    """Fixture for sample greeting data"""
    return {
        "name": "TestUser",
        "greeting_count": 1,
        "expected_message": "Hello, TestUser! 🎉"
    }
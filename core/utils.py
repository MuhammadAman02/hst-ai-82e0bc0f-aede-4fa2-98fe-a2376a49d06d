"""Utility functions for the application"""

import asyncio
import random
from datetime import datetime
from typing import List, Dict, Any

def get_current_timestamp() -> str:
    """Get current timestamp in ISO format"""
    return datetime.now().isoformat()

def get_random_color() -> str:
    """Generate a random hex color"""
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def format_greeting_count(count: int) -> str:
    """Format greeting count with ordinal suffix"""
    if 10 <= count % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(count % 10, "th")
    return f"{count}{suffix}"

async def simulate_typing_delay(text: str, delay_per_char: float = 0.05) -> None:
    """Simulate typing delay for animations"""
    await asyncio.sleep(len(text) * delay_per_char)

def validate_user_input(input_text: str) -> Dict[str, Any]:
    """Validate and sanitize user input"""
    cleaned = input_text.strip()
    
    return {
        "is_valid": bool(cleaned and len(cleaned) <= 100),
        "cleaned_text": cleaned,
        "length": len(cleaned),
        "errors": [] if cleaned and len(cleaned) <= 100 else ["Input must be 1-100 characters"]
    }
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application configuration settings"""
    
    # Server configuration
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Application settings
    app_name: str = "HST AI Greeting App"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # Environment
    environment: str = "production"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Global settings instance
settings = Settings()
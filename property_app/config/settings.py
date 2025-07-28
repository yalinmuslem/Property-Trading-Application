"""
Application configuration settings
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    # Server Configuration
    PORT = int(os.getenv("PORT", 8080))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", "a83991a9-fb6a-4a29-b822-cc3a757b2051")
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_HOURS = 24
    
    # Database Configuration
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "property_trading")
    MONGO_USERNAME = os.getenv("MONGO_USERNAME", "")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "")
    
    # Redis Configuration (for caching)
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB = int(os.getenv("REDIS_DB", 0))
    
    # File Upload
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'pdf']
    UPLOAD_PATH = "uploads"
    
    # Pagination
    DEFAULT_PAGE_SIZE = 20
    MAX_PAGE_SIZE = 100
    
    @classmethod
    def get_mongo_uri(cls):
        """Generate MongoDB connection URI"""
        if cls.MONGO_USERNAME and cls.MONGO_PASSWORD:
            return f"mongodb://{cls.MONGO_USERNAME}:{cls.MONGO_PASSWORD}@{cls.MONGO_HOST}:{cls.MONGO_PORT}/{cls.MONGO_DB_NAME}"
        else:
            return f"mongodb://{cls.MONGO_HOST}:{cls.MONGO_PORT}/{cls.MONGO_DB_NAME}"

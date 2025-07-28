"""
Database configuration and connection management
"""

import motor.motor_tornado
from config.settings import Settings

class DatabaseManager:
    _instance = None
    _client = None
    _database = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._client is None:
            self._connect()
    
    def _connect(self):
        """Initialize database connection"""
        try:
            mongo_uri = Settings.get_mongo_uri()
            self._client = motor.motor_tornado.MotorClient(mongo_uri)
            self._database = self._client[Settings.MONGO_DB_NAME]
            print(f"✅ Connected to MongoDB: {Settings.MONGO_DB_NAME}")
        except Exception as e:
            print(f"❌ Failed to connect to MongoDB: {e}")
            raise
    
    def get_database(self):
        """Get database instance"""
        return self._database
    
    def get_collection(self, collection_name):
        """Get specific collection"""
        return self._database[collection_name]
    
    async def close_connection(self):
        """Close database connection"""
        if self._client:
            self._client.close()
            print("📴 Database connection closed")

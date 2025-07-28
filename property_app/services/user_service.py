"""
User Service - Business logic for user management and authentication
"""

from datetime import datetime, timedelta
from typing import Optional, Dict, List
import jwt
from bson import ObjectId
from models.user import User
from utils.database import DatabaseManager
from config.settings import Settings

class UserService:
    def __init__(self):
        self.db = DatabaseManager().get_database()
        self.collection = self.db.users
    
    async def create_user(self, property_data: dict) -> User:
        try:
            # Get the latest user to determine the next user_id
            last_user = await self.collection.find_one(
                {}, sort=[("id", -1)]
            )
            next_user_id = 1
            if last_user and "id" in last_user:
                next_user_id = int(last_user["id"]) + 1

            property_data = {
                'name': property_data.get('name'),
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow(),
                'id': int(next_user_id)
            }

            # Create user object with 'name' and 'id'
            user = User({'name': property_data['name'], 'id': int(next_user_id)})
            now = int(datetime.utcnow().timestamp() * 1_000_000)
            user.created_at = now
            user.updated_at = now
            user.id = int(next_user_id)

            # Prepare data for insertion
            user_dict = user.to_dict()
            # Insert into database
            result = await self.collection.insert_one(user_dict)

            return user
        except Exception as e:
            raise Exception(f"Failed to create user: {str(e)}")
    
    async def get_users(self, page_num: int = 1, page_size: int = 20, id: str = None) -> Dict:
        """Get users with filtering and pagination"""
        try:
            query = {}
            if id:
                query['id'] = int(id)  # id can be None or a string

            total_count = await self.collection.count_documents(query)
            skip = (page_num - 1) * page_size
            total_pages = (total_count + page_size - 1) // page_size

            # Get users (exclude password hash)
            cursor = self.collection.find(query).sort("created_at", -1).skip(skip).limit(page_size)
            user_docs = await cursor.to_list(length=page_size)
            users = [User(doc).to_dict() for doc in user_docs]

            return users
        except Exception as e:
            raise Exception(f"Failed to get users: {str(e)}")
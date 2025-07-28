"""
User model for authentication and user management
"""

from datetime import datetime
from typing import Optional, List, Dict
import bcrypt
from marshmallow import Schema, fields, validate
from bson import ObjectId

class User:
    def __init__(self, data: dict):
        self._id = data.get('_id')
        self.id = data.get('id')
        self.name = data.get('name')
        self.created_at = data.get('created_at', datetime.utcnow())
        self.updated_at = data.get('updated_at', datetime.utcnow())  
    
    def to_dict(self):
        """Convert user to dictionary"""
        return {
            'id': int(self.id) if self.id else None,
            'name': self.name,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at,
            'updated_at': self.updated_at.isoformat() if isinstance(self.updated_at, datetime) else self.updated_at,
        }

class UserListSchema(Schema):
    """Schema for user listing queries"""
    page_num = fields.Int(validate=validate.Range(min=1), missing=1)
    page_size = fields.Int(validate=validate.Range(min=1, max=100), missing=20)
    user_id = fields.Str(allow_none=True, required=False)

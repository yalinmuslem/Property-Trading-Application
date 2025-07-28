"""
Property model for property listings
"""

from datetime import datetime
from typing import Optional, List, Dict
from marshmallow import Schema, fields, validate
from bson import ObjectId

class Property:
    def __init__(self, data: dict):
        self.id = data.get('_id')
        self.created_at = data.get('created_at', datetime.utcnow())
        self.updated_at = data.get('updated_at', datetime.utcnow())
        self.user_id = data.get('user_id')  # Assuming user_id is used for ownership
        self.listing_type = data.get('listing_type')  # Assuming listing_type is used for ownership
        self.price = data.get('price')
        self.user = data.get('user', {})  # User information if available

    def to_dict(self, is_active: bool = False):
        """Convert property to dictionary"""
        
        result = {
            'id': str(self.id) if self.id else None,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at,
            'updated_at': self.updated_at.isoformat() if isinstance(self.updated_at, datetime) else self.updated_at,
            'user_id': self.user_id if self.user_id else None,
            'listing_type': self.listing_type if self.listing_type else None,
            'price': self.price if self.price else None,
        }
        
        if is_active:
            id = self.user.get('id')
            name = self.user.get('name')
            created_at = self.user.get('created_at')
            updated_at = self.user.get('updated_at')
            
            # if id is array get first element
            if isinstance(id, list) and id:
                id = id[0]
            if isinstance(name, list) and name:
                name = name[0]
            if isinstance(created_at, list) and created_at:
                created_at = created_at[0]
            if isinstance(updated_at, list) and updated_at:
                updated_at = updated_at[0]
            
            result['user'] = {
                'id': id,
                'name': name,
                'created_at': created_at,
                'updated_at': updated_at
            }
            
            # remove user_id from result if is_active
            if 'user_id' in result:
                del result['user_id']
        
        return result

class PropertySchema(Schema):
    """Schema for property validation (POST /listings)"""
    user_id = fields.Int(required=True)
    listing_type = fields.Str(required=True)
    price = fields.Int(required=True, validate=validate.Range(min=0))

class PropertyListSchema(Schema):
    """Schema for property listing queries (GET /listings)"""
    page_num = fields.Int(validate=validate.Range(min=1), missing=1)
    page_size = fields.Int(validate=validate.Range(min=1, max=100), missing=10)
    user_id = fields.Str(allow_none=True, required=False)

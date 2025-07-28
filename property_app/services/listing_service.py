"""
Listing Service - Business logic for property listings
"""

from datetime import datetime
from typing import Optional, List, Dict
from bson import ObjectId
from models.property import Property
from utils.database import DatabaseManager

class ListingService:
    def __init__(self):
        self.db = DatabaseManager().get_database()
        self.collection = self.db.properties
        self.userCollection = self.db.users

    async def create_property(self, property_data: dict) -> Property:
        try:
            now = int(datetime.utcnow().timestamp() * 1_000_000)
            property_data = {
                'user_id': property_data.get('user_id'),
                'listing_type': property_data.get('listing_type'),
                'price': property_data.get('price'),
                'created_at': now,
                'updated_at': now
            }
            result = await self.collection.insert_one(property_data)
            property_data['_id'] = result.inserted_id
            return Property(property_data)
        except Exception as e:
            raise Exception(f"Failed to create property: {str(e)}")
            return Property(property_data)
        except Exception as e:
            raise Exception(f"Failed to create property: {str(e)}")

    async def get_properties(self, page_num: int = 1, page_size: int = 10, user_id: str = None, is_active: bool = False) -> Dict:
        try:
            query = {}

            if is_active is True and user_id:               
                q = [
                    {
                        '$match': {'user_id': int(user_id)}
                    },
                    {
                        '$lookup': {
                            'from': 'users',
                            'localField': 'user_id',
                            'foreignField': 'id',
                            'as': 'user_info'
                        }
                    },
                    {
                        '$addFields': {
                            'user': {
                                'id': '$user_info.id',
                                'name': '$user_info.name',
                                'created_at': '$user_info.created_at',
                                'updated_at': '$user_info.updated_at'
                            }
                        }
                    },
                    {
                        '$project': {
                            'user_info': 0  # remove user_info from result
                        }
                    },
                    {'$sort': {'created_at': -1}}
                ]

                cursor = self.collection.aggregate(q)
                
                q.extend([
                    {'$skip': (page_num - 1) * page_size},
                    {'$limit': page_size}
                ])
                print(f"Aggregation pipeline: {q}")

                total_count = await self.collection.count_documents({'user_id': int(user_id)})
                skip = (page_num - 1) * page_size
                total_pages = (total_count + page_size - 1) // page_size

                property_docs = await cursor.to_list(length=page_size)
                properties = [Property(doc).to_dict(is_active=True) for doc in property_docs]
            else:
                if user_id:
                    query['user_id'] = int(user_id)
                    
                print(f"Fetching properties with query: {query}, page_num: {page_num}, page_size: {page_size}")
                
                total_count = await self.collection.count_documents(query)
                skip = (page_num - 1) * page_size
                total_pages = (total_count + page_size - 1) // page_size

                cursor = self.collection.find(query).sort("created_at", -1).skip(skip).limit(page_size)
                property_docs = await cursor.to_list(length=page_size)
                properties = [Property(doc).to_dict() for doc in property_docs]

            return properties
        except Exception as e:
            raise Exception(f"Failed to get properties: {str(e)}")

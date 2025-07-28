"""
User API handlers for authentication and user management
"""

from marshmallow import ValidationError
from api.base_handler import BaseHandler
from services.user_service import UserService
from models.user import (
    UserListSchema
)

class UserListHandler(BaseHandler):
    """Handle user listing (admin only)"""
    
    async def get(self, id=None):
        """Get user by ID or list users if no ID is provided"""
        try:
            if id:
                # Get single user by ID
                user = await self.user_service.get_users(id=int(id))
                print(f"Fetching user with ID: {id}", user)
                if not user:
                    self.write_error_response("User not found", 404)
                    return
                self.write_success(
                    "user",
                    user,
                    "User retrieved successfully",
                    200
                )
            else:
                # Get list of users
                page_num = int(self.get_argument('page_num', 1))
                page_size = int(self.get_argument('page_size', 10))
                result = await self.user_service.get_users(
                    page_num=page_num,
                    page_size=page_size
                )
                self.write_success(
                    "users",
                    result,
                    "Users retrieved successfully",
                    200
                )
        except ValidationError as e:
            self.write_validation_error(e.messages)
        except Exception as e:
            self.write_error_response(str(e), 400)
    
    async def post(self):
        """Create new user (admin only)"""
        try:
             # Ensure content type is form-urlencoded
            if self.request.headers.get("Content-Type", "").startswith("application/x-www-form-urlencoded"):
                name = self.get_body_argument('name', None)
            else:
                self.write_error_response("Content-Type must be application/x-www-form-urlencoded", 400)
                return

            if not name:
                self.write_error_response("Name is required", 400)
                return

            try:
                user = await self.user_service.create_user({'name': name})
                self.write_success(
                    "user",
                    user.to_dict(),
                    "User created successfully",
                    201
                )

            except Exception as e:
                self.write_error_response(str(e), 400)
        except ValidationError as e:
            self.write_validation_error(e.messages)
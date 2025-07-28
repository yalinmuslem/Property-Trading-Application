"""
Base handler class with authentication and utilities
"""

import json
import tornado.web
from typing import Optional, Dict, Any
from services.user_service import UserService
from models.user import User

class BaseHandler(tornado.web.RequestHandler):
    """Base handler with common functionality"""
    
    def initialize(self):
        self.user_service = UserService()
        self.current_user_obj = None
         
    def write_success(self, key: Any, data: Any = None, message: str = "Success", status_code: int = 200):
        """Write successful response"""
        self.set_status(status_code)
        response = {
            "result": True,
            key: data
        }
        self.write(response)
    
    def write_error_response(self, message: str, status_code: int = 400, error_code: str = None):
        """Write error response"""
        self.set_status(status_code)
        response = {
            "success": False,
            "message": message,
            "error_code": error_code
        }
        self.write(response)
    
    def write_validation_error(self, errors: Dict):
        """Write validation error response"""
        self.set_status(422)
        response = {
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }
        self.write(response)    
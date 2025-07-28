"""
API routes configuration
"""

from api.user_handlers import (UserListHandler)
from api.property_handlers import (PropertyListHandler)

def get_routes():
    """Define all API routes"""
    return [
        (r"/users", UserListHandler),
        (r"/users/([0-9]+)", UserListHandler),        
        (r"/listings", PropertyListHandler),
        (r"/public-api/listings", PropertyListHandler),
        
    ]
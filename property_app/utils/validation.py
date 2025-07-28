"""
Validation utilities
"""

import re
from typing import Dict, Any, List

class ValidationUtils:
    
    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def is_valid_phone(phone: str) -> bool:
        """Validate phone number format"""
        # Remove all non-digit characters
        digits_only = re.sub(r'\D', '', phone)
        # Check if it's between 10-15 digits
        return 10 <= len(digits_only) <= 15
    
    @staticmethod
    def validate_password_strength(password: str) -> Dict[str, Any]:
        """Validate password strength"""
        errors = []
        
        if len(password) < 6:
            errors.append("Password must be at least 6 characters long")
        
        if not re.search(r'[A-Za-z]', password):
            errors.append("Password must contain at least one letter")
        
        if not re.search(r'\d', password):
            errors.append("Password must contain at least one digit")
        
        return {
            "is_valid": len(errors) == 0,
            "errors": errors
        }
    
    @staticmethod
    def validate_coordinates(lat: float, lng: float) -> bool:
        """Validate latitude and longitude"""
        return -90 <= lat <= 90 and -180 <= lng <= 180
    
    @staticmethod
    def sanitize_search_term(search_term: str) -> str:
        """Sanitize search term for safe regex use"""
        # Escape special regex characters
        escaped = re.escape(search_term)
        return escaped.strip()
    
    @staticmethod
    def validate_file_extension(filename: str, allowed_extensions: List[str]) -> bool:
        """Validate file extension"""
        if not filename:
            return False
        
        extension = filename.lower().split('.')[-1]
        return extension in [ext.lower() for ext in allowed_extensions]
    
    @staticmethod
    def validate_price_range(min_price: int = None, max_price: int = None) -> Dict[str, Any]:
        """Validate price range"""
        errors = []
        
        if min_price is not None and min_price < 0:
            errors.append("Minimum price cannot be negative")
        
        if max_price is not None and max_price < 0:
            errors.append("Maximum price cannot be negative")
        
        if min_price is not None and max_price is not None and min_price > max_price:
            errors.append("Minimum price cannot be greater than maximum price")
        
        return {
            "is_valid": len(errors) == 0,
            "errors": errors
        }
    
    @staticmethod
    def validate_area_range(min_area: float = None, max_area: float = None) -> Dict[str, Any]:
        """Validate area range"""
        errors = []
        
        if min_area is not None and min_area < 0:
            errors.append("Minimum area cannot be negative")
        
        if max_area is not None and max_area < 0:
            errors.append("Maximum area cannot be negative")
        
        if min_area is not None and max_area is not None and min_area > max_area:
            errors.append("Minimum area cannot be greater than maximum area")
        
        return {
            "is_valid": len(errors) == 0,
            "errors": errors
        }

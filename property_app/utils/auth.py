"""
Authentication utilities
"""

import functools
from typing import Callable, List
from models.user import UserRole

def require_auth(handler_method: Callable) -> Callable:
    """Decorator to require authentication"""
    @functools.wraps(handler_method)
    async def wrapper(self, *args, **kwargs):
        user = await self.require_authentication()
        return await handler_method(self, *args, **kwargs)
    return wrapper

def require_roles(roles: List[str]) -> Callable:
    """Decorator to require specific roles"""
    def decorator(handler_method: Callable) -> Callable:
        @functools.wraps(handler_method)
        async def wrapper(self, *args, **kwargs):
            user = await self.require_role(roles)
            return await handler_method(self, *args, **kwargs)
        return wrapper
    return decorator

def admin_required(handler_method: Callable) -> Callable:
    """Decorator to require admin role"""
    return require_roles([UserRole.ADMIN])(handler_method)

def seller_or_agent_required(handler_method: Callable) -> Callable:
    """Decorator to require seller or agent role"""
    return require_roles([UserRole.SELLER, UserRole.AGENT, UserRole.ADMIN])(handler_method)

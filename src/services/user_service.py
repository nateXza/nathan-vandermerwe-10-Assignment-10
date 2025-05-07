from typing import List, Optional
from src.models.user import User
from src.services.base_service import BaseService

class UserService(BaseService[User]):
    """Service class for handling user-related operations."""
    
    def __init__(self):
        # In a real application, this would be injected
        self._users: List[User] = []
    
    def create(self, user: User) -> User:
        """Create a new user."""
        # Validate user data
        if not user.username or not user.email:
            raise ValueError("Username and email are required")
        
        # Check if user already exists
        if any(u.email == user.email for u in self._users):
            raise ValueError("User with this email already exists")
        
        self._users.append(user)
        return user
    
    def get_by_id(self, user_id: str) -> Optional[User]:
        """Get a user by their ID."""
        return next((user for user in self._users if user.id == user_id), None)
    
    def get_all(self) -> List[User]:
        """Get all users."""
        return self._users
    
    def update(self, user_id: str, updated_user: User) -> Optional[User]:
        """Update an existing user."""
        user = self.get_by_id(user_id)
        if not user:
            return None
            
        # Update user fields
        user.username = updated_user.username
        user.email = updated_user.email
        return user
    
    def delete(self, user_id: str) -> bool:
        """Delete a user by their ID."""
        user = self.get_by_id(user_id)
        if user:
            self._users.remove(user)
            return True
        return False 
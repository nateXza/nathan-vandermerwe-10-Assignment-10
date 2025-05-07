from typing import List, Optional
from src.models.image import Image
from src.services.base_service import BaseService

class ImageService(BaseService[Image]):
    """Service class for handling image-related operations."""
    
    def __init__(self):
        # In a real application, this would be injected
        self._images: List[Image] = []
    
    def create(self, image: Image) -> Image:
        """Create a new image."""
        # Validate image data
        if not image.filename or not image.path:
            raise ValueError("Filename and path are required")
        
        # Check if image already exists
        if any(img.filename == image.filename for img in self._images):
            raise ValueError("Image with this filename already exists")
        
        self._images.append(image)
        return image
    
    def get_by_id(self, image_id: str) -> Optional[Image]:
        """Get an image by its ID."""
        return next((img for img in self._images if img.id == image_id), None)
    
    def get_all(self) -> List[Image]:
        """Get all images."""
        return self._images
    
    def update(self, image_id: str, updated_image: Image) -> Optional[Image]:
        """Update an existing image."""
        image = self.get_by_id(image_id)
        if not image:
            return None
            
        # Update image fields
        image.filename = updated_image.filename
        image.path = updated_image.path
        return image
    
    def delete(self, image_id: str) -> bool:
        """Delete an image by its ID."""
        image = self.get_by_id(image_id)
        if image:
            self._images.remove(image)
            return True
        return False 
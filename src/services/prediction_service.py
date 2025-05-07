from typing import List, Optional
from src.models.prediction import Prediction
from src.services.base_service import BaseService

class PredictionService(BaseService[Prediction]):
    """Service class for handling prediction-related operations."""
    
    def __init__(self):
        # In a real application, this would be injected
        self._predictions: List[Prediction] = []
    
    def create(self, prediction: Prediction) -> Prediction:
        """Create a new prediction."""
        # Validate prediction data
        if not prediction.result:
            raise ValueError("Prediction result is required")
        
        self._predictions.append(prediction)
        return prediction
    
    def get_by_id(self, prediction_id: str) -> Optional[Prediction]:
        """Get a prediction by its ID."""
        return next((pred for pred in self._predictions if pred.id == prediction_id), None)
    
    def get_all(self) -> List[Prediction]:
        """Get all predictions."""
        return self._predictions
    
    def update(self, prediction_id: str, updated_prediction: Prediction) -> Optional[Prediction]:
        """Update an existing prediction."""
        prediction = self.get_by_id(prediction_id)
        if not prediction:
            return None
            
        # Update prediction fields
        prediction.result = updated_prediction.result
        return prediction
    
    def delete(self, prediction_id: str) -> bool:
        """Delete a prediction by its ID."""
        prediction = self.get_by_id(prediction_id)
        if prediction:
            self._predictions.remove(prediction)
            return True
        return False 
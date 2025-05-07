from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uuid

from src.services.user_service import UserService
from src.services.image_service import ImageService
from src.services.prediction_service import PredictionService
from src.models.user import User
from src.models.image import Image
from src.models.prediction import Prediction

app = FastAPI(
    title="Image Analysis API",
    description="API for managing users, images, and predictions",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
user_service = UserService()
image_service = ImageService()
prediction_service = PredictionService()

# Pydantic models for request/response
class UserCreate(BaseModel):
    username: str
    email: str

class ImageCreate(BaseModel):
    filename: str
    path: str

class PredictionCreate(BaseModel):
    result: str

# User endpoints
@app.post("/api/users", response_model=User, tags=["Users"])
async def create_user(user: UserCreate):
    try:
        new_user = User(id=str(uuid.uuid4()), username=user.username, email=user.email)
        return user_service.create(new_user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/users", response_model=List[User], tags=["Users"])
async def get_users():
    return user_service.get_all()

@app.get("/api/users/{user_id}", response_model=User, tags=["Users"])
async def get_user(user_id: str):
    user = user_service.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/api/users/{user_id}", response_model=User, tags=["Users"])
async def update_user(user_id: str, user: UserCreate):
    updated_user = User(id=user_id, username=user.username, email=user.email)
    result = user_service.update(user_id, updated_user)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result

@app.delete("/api/users/{user_id}", tags=["Users"])
async def delete_user(user_id: str):
    if not user_service.delete(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

# Image endpoints
@app.post("/api/images", response_model=Image, tags=["Images"])
async def create_image(image: ImageCreate):
    try:
        new_image = Image(id=str(uuid.uuid4()), filename=image.filename, path=image.path)
        return image_service.create(new_image)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/images", response_model=List[Image], tags=["Images"])
async def get_images():
    return image_service.get_all()

@app.get("/api/images/{image_id}", response_model=Image, tags=["Images"])
async def get_image(image_id: str):
    image = image_service.get_by_id(image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return image

@app.put("/api/images/{image_id}", response_model=Image, tags=["Images"])
async def update_image(image_id: str, image: ImageCreate):
    updated_image = Image(id=image_id, filename=image.filename, path=image.path)
    result = image_service.update(image_id, updated_image)
    if not result:
        raise HTTPException(status_code=404, detail="Image not found")
    return result

@app.delete("/api/images/{image_id}", tags=["Images"])
async def delete_image(image_id: str):
    if not image_service.delete(image_id):
        raise HTTPException(status_code=404, detail="Image not found")
    return {"message": "Image deleted successfully"}

# Prediction endpoints
@app.post("/api/predictions", response_model=Prediction, tags=["Predictions"])
async def create_prediction(prediction: PredictionCreate):
    try:
        new_prediction = Prediction(id=str(uuid.uuid4()), result=prediction.result)
        return prediction_service.create(new_prediction)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/predictions", response_model=List[Prediction], tags=["Predictions"])
async def get_predictions():
    return prediction_service.get_all()

@app.get("/api/predictions/{prediction_id}", response_model=Prediction, tags=["Predictions"])
async def get_prediction(prediction_id: str):
    prediction = prediction_service.get_by_id(prediction_id)
    if not prediction:
        raise HTTPException(status_code=404, detail="Prediction not found")
    return prediction

@app.put("/api/predictions/{prediction_id}", response_model=Prediction, tags=["Predictions"])
async def update_prediction(prediction_id: str, prediction: PredictionCreate):
    updated_prediction = Prediction(id=prediction_id, result=prediction.result)
    result = prediction_service.update(prediction_id, updated_prediction)
    if not result:
        raise HTTPException(status_code=404, detail="Prediction not found")
    return result

@app.delete("/api/predictions/{prediction_id}", tags=["Predictions"])
async def delete_prediction(prediction_id: str):
    if not prediction_service.delete(prediction_id):
        raise HTTPException(status_code=404, detail="Prediction not found")
    return {"message": "Prediction deleted successfully"} 
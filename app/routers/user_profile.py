from fastapi import APIRouter, Depends, UploadFile
import app.controllers.user_profile as controller
from app.controllers.cognito import get_current_user
import app.models.model_types as model_type
from typing import List

router = APIRouter()

@router.post("/user_profile")
async def create_user_profile(user_profile : model_type.UserProfile,
    user: dict = Depends(get_current_user)):
    try:
        user_id = user.get('login_id')
        user_pro = await controller.user_profile(user_id,user_profile)
        response = {
            "status": True,
            "message": "Profile Created successfully",
            "data": user_pro
        }
        return response
    except Exception as e:
        return {
            "status": False,
            "message": "An error occurred while creating profile.",
            "data": None
        }

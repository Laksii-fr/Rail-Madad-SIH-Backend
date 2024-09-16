from fastapi import APIRouter, File, UploadFile, Form, Depends
from app.controllers.cognito import get_current_user
import app.controllers.misc as misc
import app.models.model_types as model
from typing import *
router = APIRouter()

@router.post("/suggestion/")
async def suggestion(
    message: str = Form(...),
    suggestion_type: Literal[
    "New Train",
    "New Stoppage",
    "Passenger Amenities",
    "Freight Services",
    "High Speed Rail Travel",
    "Infusing Technology",
    "Reducing Carbon Footprint",
    "Others"
] = Form(...),
    user: dict = Depends(get_current_user),
):
    try:
        user_id = user.get('login_id')
        suggestion = await misc.suggestion(user_id,suggestion_type,message)
        response = {
            "status": True,
            "message": "Suggestion Saved Successfully",
            "data": suggestion
        }
        return response
    except Exception as e:
        return {
            "status": False,
            "message": f"An error occurred {e}",
            "data": None
        }

@router.post("/anubhav/")
async def anubhav(
    anubhav : model.SubmittAnubhav = Depends(),
    user: dict = Depends(get_current_user),
):
    try:
        user_id = user.get('login_id')
        anubhav = await misc.anubhav(user_id,anubhav)
        response = {
            "status": True,
            "message": "User Anubhav Saved successfully",
            "data": anubhav
        }
        return response
    except Exception as e:
        return {
            "status": False,
            "message": f"An error occurred while creating chat.{e}",
            "data": None
        }

@router.post("/get-all-anubhav/")
async def get_anubhav(user: dict = Depends(get_current_user)):
    try:
        user_id = user.get('login_id')
        anubhav = await misc.get_all_anubhav(user_id)
        response = {
            "status": True,
            "message": "User Anubhav Saved successfully",
            "data": anubhav
        }
        return response
    except Exception as e:
        return {
            "status": False,
            "message": f"An error occurred while creating chat.{e}",
            "data": None
        }
    
@router.post("/get-all-suggestions/")
async def get_suggestion(user: dict = Depends(get_current_user)):
    try:
        user_id = user.get('login_id')
        anubhav = await misc.get_all_anubhav(user_id)
        response = {
            "status": True,
            "message": "User Anubhav Saved successfully",
            "data": anubhav
        }
        return response
    except Exception as e:
        return {
            "status": False,
            "message": f"An error occurred while creating chat.{e}",
            "data": None
        }
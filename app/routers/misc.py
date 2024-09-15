from fastapi import APIRouter, File, UploadFile, Form, Depends
from app.controllers.cognito import get_current_user
import app.controllers.chat as chat

router = APIRouter()

@router.post("/suggestion/")
async def suggestion(
    message: str = Form(...),
    user: dict = Depends(get_current_user),
):
    try:
        user_id = user.get('login_id')
        chat_response = await chat.send_topic_to_api(user_id,message)
        print(chat_response)
        response = {
            "status": True,
            "message": "Chat Created successfully",
            "data": chat_response
        }
        return response
    except Exception as e:
        return {
            "status": False,
            "message": f"An error occurred while creating chat.{e}",
            "data": None
        }

@router.post("/anubhav/")
async def anubhav(
    message: str = Form(...),
    user: dict = Depends(get_current_user),
):
    try:
        user_id = user.get('login_id')
        chat_response = await chat.send_topic_to_api(user_id,message)
        print(chat_response)
        response = {
            "status": True,
            "message": "Chat Created successfully",
            "data": chat_response
        }
        return response
    except Exception as e:
        return {
            "status": False,
            "message": f"An error occurred while creating chat.{e}",
            "data": None
        }

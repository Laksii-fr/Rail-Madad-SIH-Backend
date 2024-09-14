from fastapi import APIRouter, File, UploadFile, Form, Depends
from app.controllers.cognito import get_current_user
import app.controllers.chat as chat

router = APIRouter()

@router.post("/create-chat/")
async def send_message(
    message: str = Form(...),
    user: dict = Depends(get_current_user),
    threadToken: str = Form(None),
    image: UploadFile = File(None)
    
):
    try:
        user_id = user.get('login_id')
        chat_response = chat.send_message_to_api(message, threadToken, image)
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

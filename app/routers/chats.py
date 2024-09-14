from fastapi import APIRouter, File, UploadFile, Form, Depends
from app.controllers.cognito import get_current_user
import app.controllers.chat as controller
import app.models.model_types as modelType
router = APIRouter()

@router.post("/create-chat/")
async def send_message(
    chat : modelType.CreateChat = Depends(),
    user: dict = Depends(get_current_user),
    image: UploadFile = File(None)
    
):
    try:
        user_id = user.get('login_id')
        chat_response = await controller.send_message_to_api(user_id,chat.message, chat.threadToken, image)
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
    
@router.post("/issue-prioritizer/")
async def prioritizer(
    issue : modelType.Prioritizer = Depends(),
    user: dict = Depends(get_current_user),
):
    try:
        user_id = user.get('login_id')
        chat_response = await controller.send_topic_to_api(user_id,issue)
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

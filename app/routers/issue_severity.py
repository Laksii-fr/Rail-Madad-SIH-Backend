from fastapi import APIRouter, File, UploadFile, Form, Depends
from app.controllers.cognito import get_current_user
import app.utils.mongo_utils as mongo

router = APIRouter()

@router.post("/get-all-issues/")
async def send_message(
    user: dict = Depends(get_current_user),
    issue_severity: int = Form(None)
):
    try:
        user_id = user.get('login_id')
        chat_response = mongo.fetch_all_issue(user_id,issue_severity)
        response = {
            "status": True,
            "message": "Issues Fetched successfully",
            "data": chat_response
        }
        return response
    except Exception as e:
        return {
            "status": False,
            "message": f"An error occurred while creating chat.{e}",
            "data": None
        }
    
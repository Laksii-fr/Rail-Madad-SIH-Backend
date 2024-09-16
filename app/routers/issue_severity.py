from fastapi import APIRouter, File, UploadFile, Form, Depends
from app.controllers.cognito import get_current_user
import app.utils.mongo_utils as mongo

router = APIRouter()


    
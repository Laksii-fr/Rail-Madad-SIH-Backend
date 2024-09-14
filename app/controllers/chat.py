from fastapi import APIRouter, File, UploadFile, Form, Depends
import app.utils.mongo_utils as mongo
import app.helpers.api_helper as helper
import requests,os

API_URL = os.getenv('API_URL')
DEFAULT_AST_NAME = os.getenv('DEFAULT_AST_NAME')
DEFAULT_API_TOKEN = os.getenv('DEFAULT_API_TOKEN')
DEFAULT_TOPIC_AST_NAME = os.getenv('DEFAULT_TOPIC_AST_NAME')
DEFAULT_TOPIC_API_TOKEN = os.getenv('DEFAULT_TOPIC_API_TOKEN')

async def send_message_to_api(userId, message: str, ThreadToken: str = None, image: UploadFile = None):
    response = await helper.send_message(message,ThreadToken,image)
    if response.get("status") and response.get("data") and response.get("thread_data"):
        message = response["data"][0][0]["message"]
        thread_id = response["data"][0][0]["thread_id"]
        threadToken = response["thread_data"][0]["threadToken"]
        threadTitle = response["thread_data"][0]["threadTitle"]
    if not ThreadToken:
        mongo.save_user_thread(userId,thread_id,threadToken,threadTitle)

        # Return the extracted data
    return {
        "message": message,
        "thread_id": thread_id,
        "threadToken": threadToken,
        "threadTitle": threadTitle
    }
    # return response

async def send_topic_to_api(userId,message: str):
    data_message = await helper.send_topic_to_api(message)
    mongo.save_issue_priority(userId,message,data_message)
    return data_message
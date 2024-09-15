from fastapi import APIRouter, File, UploadFile, Form, Depends
import app.utils.mongo_utils as mongo
import app.helpers.api_helper as helper
import requests,os

API_URL = os.getenv('API_URL')
DEFAULT_AST_NAME = os.getenv('DEFAULT_AST_NAME')
DEFAULT_API_TOKEN = os.getenv('DEFAULT_API_TOKEN')
DEFAULT_TOPIC_AST_NAME = os.getenv('DEFAULT_TOPIC_AST_NAME')
DEFAULT_TOPIC_API_TOKEN = os.getenv('DEFAULT_TOPIC_API_TOKEN')

async def send_message_to_api(userId, issue_type, message: str, ThreadToken: str = None, image: UploadFile = None):
    message = f"{message} - my issue is regarding: {issue_type}"
    
    # Send the message using helper
    response = await helper.send_message(message, ThreadToken, image)
    
    if response.get("status") and response.get("data") and response.get("thread_data"):
        message_data = response["data"][0][0]
        thread_data = response["thread_data"][0]
        
        # Extract message and thread details safely
        message = message_data.get("message", "No message found")
        thread_id = message_data.get("thread_id", None)
        threadToken = thread_data.get("threadToken", None)
        threadTitle = thread_data.get("threadTitle", None)
        
        # Check if thread_id and threadToken exist before saving to MongoDB
        if thread_id and threadToken:
            mongo.save_user_thread(userId, issue_type, thread_id, threadToken, threadTitle)
            
        # Return the extracted data
        return {
            "message": message,
            "thread_id": thread_id,
            "threadToken": threadToken,
            "threadTitle": threadTitle
        }
    else:
        # Handle case where response doesn't have expected data
        raise ValueError("Unexpected response format from helper.send_message")
    # return response

async def send_topic_to_api(userId,message: str):
    print("1")
    data_message = await helper.send_topic_to_api(message)
    print("2")
    mongo.save_issue_priority(userId,message,data_message)
    return data_message
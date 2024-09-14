from fastapi import APIRouter, File, UploadFile, Form, Depends
import requests,os

API_URL = os.getenv('API_URL')
DEFAULT_AST_NAME = os.getenv('DEFAULT_AST_NAME')
DEFAULT_API_TOKEN = os.getenv('DEFAULT_API_TOKEN')

async def send_message_to_api(message: str, threadToken: str = None, image: UploadFile = None):
    # Prepare the data to be sent in the request
    data = {
        'astName': DEFAULT_AST_NAME,
        'apiToken': DEFAULT_API_TOKEN,
        'message': message
    }
    
    # Add the threadToken if it exists
    if threadToken:
        data['threadtoken'] = threadToken

    # Prepare the files to be sent
    files = {}
    if image:
        files['image'] = (image.filename, image.file, image.content_type)
    
    # Send the request using the requests library
    response = requests.post(API_URL, data=data, files=files)
    
    # Return the response as JSON
    return response.json()
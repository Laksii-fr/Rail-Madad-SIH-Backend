from fastapi import APIRouter, File, UploadFile, Form, Depends
import requests,os

API_URL = os.getenv('API_URL')
DEFAULT_AST_NAME = os.getenv('DEFAULT_AST_NAME')
DEFAULT_API_TOKEN = os.getenv('DEFAULT_API_TOKEN')
DEFAULT_TOPIC_AST_NAME = os.getenv('DEFAULT_TOPIC_AST_NAME')
DEFAULT_TOPIC_API_TOKEN = os.getenv('DEFAULT_TOPIC_API_TOKEN')

async def send_message(message: str, threadToken: str = None, image: UploadFile = None):
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
    # return {
    #     "response" : response.json(),
    #     "thread_token" : data['threadtoken']
    #     }
    return response.json()

async def send_topic_to_api(message: str):
    # Prepare the data to be sent in the request
    data = {
        'astName': DEFAULT_TOPIC_AST_NAME,
        'apiToken': DEFAULT_TOPIC_API_TOKEN,
        'message': message
    }
    # Send the request using the requests library
    response = requests.post(API_URL, data=data)
    
    # Parse the response JSON
    chat_response = response.json()
    
    # Extract the 'message' field from the response
    data_message = chat_response['data'][0][0]['message']
    
    return data_message
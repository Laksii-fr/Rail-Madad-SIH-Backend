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
    return response.json()

import requests

import requests

async def send_topic_to_api(message: str):
    # Prepare the data to be sent in the request
    print("1.1")
    data = {
        'astName': DEFAULT_TOPIC_AST_NAME,
        'apiToken': DEFAULT_TOPIC_API_TOKEN,
        'message': message
    }
    print("1.2")
    
    # Send the request using the requests library
    response = requests.post(API_URL, data=data)
    print("1.3")
    
    # Parse the response JSON
    try:
        chat_response = response.json()  # Parse the JSON response
        print("chat_response:", chat_response)  # Inspect the response
        
        # Ensure 'data' exists and is a list
        if 'data' not in chat_response or not isinstance(chat_response['data'], list):
            raise ValueError("Invalid 'data' format in response.")
        
        # Extract the 'message' field
        data_message = chat_response['data'][0][0]['message']  # Access the "message"
        print("Extracted message:", data_message)
        return data_message
    
    except ValueError as e:
        print(f"An error occurred: {e}")
    except KeyError as e:
        print(f"KeyError: Missing {e} in the response")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



# def send_topic_to_api(message: str):
#     # Prepare the data to be sent in the request
#     data = {
#         'astName': DEFAULT_TOPIC_AST_NAME,
#         'apiToken': DEFAULT_TOPIC_API_TOKEN,
#         'message': message
#     }
    
#     # Send the request using the requests library
#     response = requests.post(API_URL, data=data)
    
#     # Parse the response JSON
#     chat_response = response.json()
    
#     # Extract the specific 'message' from the 'data' section
#     # Assuming the 'data' structure as: [['{'id': ..., 'message': '8', ...}']]
#     data_message = chat_response['data'][0][0]['message']
    
#     return data_message
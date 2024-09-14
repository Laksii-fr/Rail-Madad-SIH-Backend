from app.database import UsersCollection
from app.database import UserThreads
from app.database import UserProfiles,IssuePriority
from datetime import datetime
from fastapi import HTTPException, status
import app.models.model_types as modelType
from datetime import datetime

def save_user_info(email: str, sub_id: str = None, is_confirmed: bool = False):
    try:
        # Define the update operation
        update_operation = {
            "email": email,
            "is_confirmed": is_confirmed
        }

        # Only update sub_id if it is provided
        if sub_id:
            update_operation["sub_id"] = sub_id

        # Use upsert=True to create the document if it doesn't exist
        UsersCollection.update_one(
            {"email": email},
            {"$set": update_operation},
            upsert=True
        )

    except Exception as e:
        print(f"Error saving user info: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred while saving user info: {str(e)}")

def find_user_by_email(email: str):
    """Find a user by email."""
    return UsersCollection.find_one({"email": email})

def insert_new_user(email: str, sub_id: str, is_confirmed: bool = False):
    """Insert a new user into the database."""
    user_data = {
        "email": email,
        "sub_id": sub_id,
        "is_confirmed": is_confirmed
    }
    return UsersCollection.insert_one(user_data)

def update_user_confirmation_status(email: str, is_confirmed: bool):
    """Update the confirmation status of a user."""
    return UsersCollection.update_one(
        {"email": email},
        {"$set": {"is_confirmed": is_confirmed}}
    )

def save_user_profile(userId, payload: modelType.UserProfile):
    new_profile = {
        "userID": userId,
        "UserName": payload.User_name,
        "UserMail": payload.User_email,
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
    }  # type: ignore

    try:
        # Update the existing profile if it exists, otherwise insert a new one
        result = UserProfiles.update_one(
            {"userID": userId},  # Filter to find the existing profile by userID
            {"$set": new_profile},  # Set the new data
            upsert=True  # Insert if not found
        )

        if result.matched_count:
            print(f"User profile with userID {userId} updated successfully.")
        else:
            print(f"New user profile with userID {userId} created successfully.")

    except Exception as e:
        print(f"Error {e}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Something went wrong during saving user profile in database.",
        )
def save_user_thread(userId,thread_id,threadtoken,threadTitle):
    new_threads = {
        "userId": userId,
        "Thread_id" : thread_id,
        "ThreadToken" : threadtoken,
        "threadTitle" : threadTitle,
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
    }  # type: ignore
    try:
        UserThreads.insert_one(new_threads)
    except Exception as e:
        print(f"Error {e}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Something went wrong during saving assistant in database.{e}",
        )

def save_issue_priority(userId,Issue : modelType.Prioritizer,rate):
    new_details = {
        "userId": userId,
        "category" : Issue.category,
        "Issue_Title" : Issue.message,
        "Issue_Severity": rate
    }
    try:
        IssuePriority.insert_one(new_details)
    except Exception as e:
        print(f"Error {e}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Something went wrong during saving assistant in database.{e}",
        )
    
def fetch_all_issue(user_id: str,Issue_Severity = None):
    try:
        # Base filter for user ID
        filter_conditions = {"userId": user_id}
        
        # Add search functionality for astName (case-insensitive regex search)
        if Issue_Severity:
            filter_conditions["Issue_Severity"] = {"$regex": Issue_Severity, "$options": "i"}

        # Always sort by createdAt in descending order
        cur = IssuePriority.find(
            filter=filter_conditions, 
            projection={
                "_id": 0, 
                "userId" : 1,
                "Issue_Title" : 1,
                "Issue_Severity" : 1
            }
        ).sort([("createdAt", -1)])

        # Convert cursor to list
        result = [doc for doc in cur]

        return result
    
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Something went wrong during fetching assistants.{e}",
        )

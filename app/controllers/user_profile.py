import app.models.model_types as model_type
import app.utils.mongo_utils as mongo
from typing import *


async def user_profile(user_id , user_profile : model_type.UserProfile):
    mongo.save_user_profile(user_id,user_profile)
    return user_profile
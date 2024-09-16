import app.models.model_types as model_type
import app.utils.mongo_utils as mongo
from typing import *

async def suggestion(userId,suggestion_type,message):
    saved_suggestion = mongo.save_suggestion(userId,suggestion_type,message)
    return saved_suggestion

async def anubhav(userId,Anubhav : model_type.SubmittAnubhav):
    saved_Anubhav = mongo.save_anubhav(userId,Anubhav)
    return saved_Anubhav

async def get_all_anubhav(userId):
    get_all_Anubhav = mongo.get_all_Anubhav(userId)
    return get_all_Anubhav

async def get_all_Suggestions(userId):
    get_all_Suggesitons = mongo.get_all_Suggestions(userId)
    return get_all_Suggesitons
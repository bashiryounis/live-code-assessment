from pydantic import BaseModel
from  datetime import datetime
# TODO: Create the pydantic schemas for the endpoints (use models.py as reference)

class Context(BaseModel): 
    topic:str 
    location:str 
    language:str 

class Tweet(BaseModel):
    tweet:str 
    context:Context 
    author_name:str 
    author_email:str 

class TweetRequest(Context):
    pass

class TweetResponse(Tweet): 
    id: int 
    created_at:datetime 

    class Config:
        orm_mode = True

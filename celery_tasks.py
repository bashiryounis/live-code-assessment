import os
import time 
from celery import Celery
from config import settings
from models import Tweet, get_db

celery = Celery(
    "genai",
    broker = settings.CELERY_BROKER_URL,
    backend= settings.CELERY_RESULT_BACKEND,
)

@celery.task(name="delete_duplicate_tweet")
def delete_duplicate_tweet(author_email:str): 
    db = get_db()
    db_tweet = db.query(Tweet).filter(Tweet.author_email == author_email).order_by(Tweet.created_at.asc()).first()
    if db_tweet: 
        db.delete(db_tweet)
        db.commit()
        print(f"Delete duplicate tweet  by author with {author_email}")
    else  : 
        print("no duplicate Found") 




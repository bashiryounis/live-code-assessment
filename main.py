from fastapi import FastAPI, Depends, HTTPException, status
from models import create_tables, get_db, Tweet
from contextlib import asynccontextmanager
from sqlalchemy.orm import sessionmaker
from schemas import TweetRequest, TweetResponse
from sqlmodel import select
from config import settings
from ai import FakeAI
from datetime import datetime
from celery_tasks import delete_duplicate_tweet
from sqlalchemy import asc, desc

def validate_key(api_key:str): 
    if api_key != settings.X_API_KEY: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
    
    return api_key 


# Create tables on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "Welcome to INTO AI Assessment"}


# TODO: Create an endpoint to generate ai response then save it to the database (use the ai.py and models.py file)

@app.post("/generate")
async def generate(
    tweet_data:TweetRequest, 
    session: sessionmaker = Depends(get_db),
    api_key: str = Depends(validate_key)
)->TweetResponse :
    fake_ai = FakeAI()
    context = {
        "topic": tweet_data.topic,
        "location": tweet_data.location,
        "language": tweet_data.language,
    }
    generate = await fake_ai.generate_response(context)
    db_tweet = Tweet(
        tweet=generate["tweet"],
        context=f"topic={context['topic']}, location={context['location']}, language={context['language']}",
        author_name=generate.get("author_name", "FakeBot"),
        author_email=generate.get("author_email", "fakebot@example.com"),
        created_at=datetime.utcnow(),
    )
    session.add(db_tweet)
    session.commit()
    session.refresh(db_tweet)
    delete_duplicate_tweet.delay(db_tweet.author_email)
    return db_tweet


# TODO: Retrieve all tweets from the database, sorted by author name (ascending) and created_at (descending).

@app.get("/tweets", response_model=list[TweetResponse])
async def get_tweets(
    session: sessionmaker = Depends(get_db)
):
    result = session.execute(
        select(Tweet).order_by(asc(Tweet.author_name), desc(Tweet.created_at))
    )
    tweets = result.scalars().all()
    return [TweetResponse(id=tweet.id,tweet=tweet.tweet,context=tweet.context,author_name=tweet.author_name, author_email=tweet.author_email, created_at=tweet.created_at) for tweet in tweets]


from fastapi import FastAPI
from models import create_tables
from contextlib import asynccontextmanager




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




# TODO: Retrieve all tweets from the database, sorted by author name (ascending) and created_at (descending).


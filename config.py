from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

load_dotenv(verbose=True)
# TODO: Create the settings class to read environment variables

class Settings(BaseSettings):
    X_API_KEY : str = Field(env="X_API_KEY")
    CELERY_BROKER_URL: str=Field(env="CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND: str=Field(env="CELERY_RESULT_BACKEND")

settings = Settings()
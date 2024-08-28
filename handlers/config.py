import os
import pathlib
from functools import lru_cache
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

basedir = pathlib.Path(__file__).parents[1]
load_dotenv(basedir/".env")

class Settings(BaseSettings):
  """Main Settings"""
  app_name: str = "roomApp"
  env: str = os.getenv("ENV", "development")
  ### needed for CORS
  frontend_url: str = os.getenv("FRONTEND_URL", "NA")

@lru_cache
def get_settings() -> Settings:
  """Retrieve the fastapi settings"""
  return Settings()



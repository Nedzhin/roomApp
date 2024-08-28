from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def hello():
  """"Hello world route to make sure that app works correctly"""
  return {"msg": "Hello World!"}



from fastapi import APIRouter
from services.get_user import get_user as get_user_crud
from services.get_user import get_user_filter, get_filtered_profiles
from firebase_admin.exceptions import FirebaseError
from fastapi.exceptions import HTTPException
from typing import Optional

router = APIRouter()

@router.get("/user/{user_tid}")
def get_user(user_tid: str):
    try:
        res = get_user_crud(user_tid=user_tid)
        if not res:
            raise HTTPException(status_code=404)
        return res
    except FirebaseError as e:
        raise HTTPException(status_code=401, detail=e.message)
    
@router.get('/filter_profiles/{request_id}')
def filter_profiles(status: Optional[str] = None, gender: Optional[str] = None, age: Optional[int] = None, city: Optional[str] = None, request_id: Optional[str] = None):
    try:
        res_filter = get_user_filter(status=status, gender=gender, age = age, city=city, request_id=request_id)
        if not res_filter:
            raise HTTPException(status_code=404)
        return res_filter
    except FirebaseError as e:
        raise HTTPException(status_code=401, detail=e.message)
    
@router.get('/get_filtered_profiles/{request_id}')
def filter_profiles( request_id: str):
    try:
        res_profiles = get_filtered_profiles( request_id=request_id)
        if not res_profiles:
            raise HTTPException(status_code=404)
        return res_profiles
    except FirebaseError as e:
        raise HTTPException(status_code=401, detail=e.message)
    
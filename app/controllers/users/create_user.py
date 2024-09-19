from fastapi import APIRouter
from services.create_user import create_user as create_user_crud
from services.create_user import create_user_rent, create_user_travel
from fastapi.exceptions import HTTPException
from models.user import User, Rent, Travel
import uuid

router = APIRouter()

@router.post("/user")
def create_user(user: User):
    print("entered  to controller")
    try:
        return create_user_crud( 
            #id=str(uuid.uuid4()),
            **user.model_dump(),  
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail=e)
    
@router.post("/purpose/rent/{user_tid}")
def save_rent_purpose(user_tid: str, purpose: Rent):
    print("entered to rent register")
    try:
        return create_user_rent(user_tid=user_tid, **purpose.model_dump())
    except Exception as e:
        raise HTTPException(status_code=401, detail=e)

@router.post("/purpose/travel/{user_tid}")
def save_rent_purpose(user_tid: str, purpose: Travel):
    print("entered to travel register")
    try:
        return create_user_travel(user_tid=user_tid, **purpose.model_dump())
    except Exception as e:
        raise HTTPException(status_code=401, detail=e)
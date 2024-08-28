from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from models.user import User
from services.update_user import update_user as update_user_crud

router = APIRouter()

@router.put("/user/{id}/")
def update_user(id: str, user: User):
    try:
        return update_user_crud(
            id=id,
            **user.model_dump()
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail=e)
    
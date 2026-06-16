from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("")
def get_users():
    return {"endpoint": "users"}

#Ex.3
@router.get("/{user_id}")
def get_user_by_id(user_id: int):
    return {"user_id": user_id}
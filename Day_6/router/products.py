from fastapi import APIRouter

router2 = APIRouter(prefix="/products", tags=["Products"])

@router2.get("")
def get_products():
    return {"endpoint": "products"}
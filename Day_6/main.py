from fastapi import FastAPI
from .router import products, users

app = FastAPI()

#Ex.1
@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

#Ex. 2
app.include_router(products.router2)
app.include_router(users.router)
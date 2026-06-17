from fastapi import FastAPI, Depends, Request, Response, File, UploadFile, BackgroundTasks
from .router import products, users
from pydantic_settings import BaseSettings, SettingsConfigDict
import time
from fastapi.exceptions import RequestValidationError
from fastapi.responses  import JSONResponse
from pathlib import Path
import asyncio

app = FastAPI()

#Ex.1
@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

#Ex. 2
app.include_router(products.router2)
app.include_router(users.router)

#Ex.12
def get_current_user() -> dict:
    return {"username": "admin"}

@app.get("/profile")
def get_profile(current_user: dict = Depends(get_current_user)):
    return current_user

#Ex.14
class Settings(BaseSettings):
    app_name: str = "FastAPI Demo"
    debug: bool = True
    model_config = SettingsConfigDict(env_file = ".env")

settings = Settings()

@app.get("/config")
def get_config():
    return {"app_name": settings.app_name}

#Ex.15
@app.middleware("http")
async def measure_processing_time(request: Request, call_next):
    start = time.perf_counter()
    response: Response = await call_next(request)
    elapsed = time.perf_counter() - start
    response.headers["X-Process-Time"] = f"{elapsed:.6f}"
    return response

#Ex.16
@app.exception_handler(RequestValidationError)
async def custom_exception_handler(request, exc):
    return JSONResponse(
        status_code = 422,
        content = {"success": False, "message": "Validation failed"}
    )
    
#Ex.17
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok = True)

@app.post("/upload", status_code = 201)
async def upload_file(file: UploadFile = File(...)):
    dest = UPLOAD_DIR / file.filename
    content = await file.read()
    dest.write_bytes(content)
    return {"filename": file.filename}

#Ex.18
def send_email(email: str) -> None:
    time.sleep(1)
    print(f"[bg] Email sent to {email}")

@app.post("/send-email")
def send_email(background_tasks: BackgroundTasks, email: str = "user@example.com"):
    background_tasks.add_task(send_email, email)
    return {"message": "Email queued"}

#Ex.19
@app.get("/async-demo")
async def async_demo():
    await asyncio.sleep(2)
    return {"message": "Completed"}
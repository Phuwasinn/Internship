from fastapi import FastAPI, APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from .database import engine, Base
from .routers import user, post, auth
from .dependencies import get_current_user
from .models import User
import logging, time
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from .limiter import limiter
from .schemas import err, ok

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s %(levelname)-8s %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("api")

app = FastAPI(
    title = "Blog API",
    description = """
    Blog API built with FastAPI.

    Features:
    - User Management
    - Blog Posts
    - JWT Authentication
    - Role-based Authorization
    - Pagination, Filtering, Searching
    """,
    version="1.0.0",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"→  {request.method}  {request.url.path}")
    start    = time.perf_counter()
    response = await call_next(request)
    elapsed  = time.perf_counter() - start
    logger.info(f"←  {response.status_code}  ({elapsed*1000:.1f} ms)")
    return response

@app.exception_handler(Exception)
async def log_exceptions(
    request: Request,
    exc: Exception
):
    logger.error(
        f"Exception: {str(exc)}",
        exc_info = True
    )

    return JSONResponse(
        status_code = 500,
        content = err(
            "Internal Server Error"
        ).model_dump()
    )
    
@app.exception_handler(HTTPException)
async def http_exception_handler(
    request: Request,
    exc: HTTPException
):
    logger.warning(
        f"HTTP {exc.status_code}: {exc.detail}"
    )

    return JSONResponse(
        status_code = exc.status_code,
        content = err(exc.detail).model_dump()
    )

#Ex.1
@app.get("/")
def root():
    return ok(
        message = "Database connected"
    )

Base.metadata.create_all(bind = engine)

#Ex.3
app.include_router(user.router)
#Ex.5
app.include_router(post.router)
#Ex.9-11
app.include_router(auth.router)

@app.get(
    "/profile",
    summary = "Get profile",
    description = "Retrieve current authenticated user profile"
)
def profile(
    current_user: User = Depends(
        get_current_user
    )
):
    return current_user

import logging
import logging.config
import os
import time

from fastapi import Depends, FastAPI, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.v1.routes import router
from app.core.settings import settings
from app.db.database import Base, create_database, engine
from app.middleware.auth_middleware import AuthMiddleware
from app.middleware.logging_middleware import LoggingMiddleware

# Log konfiguratsiyasini yuklash
log_config_path = os.path.join(os.path.dirname(__file__), "core/logging.conf")
logging.config.fileConfig(log_config_path, disable_existing_loggers=False)

logger = logging.getLogger("uvicorn")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    docs_url=None,  # Swagger UI
    redoc_url=None,  # ReDoc
    openapi_url="/openapi.json",  # OpenAPI schema
    description=settings.DESCRIPTION,
    contact={
        "name": settings.PROJECT_NAME,
        "email": settings.PROJECT_EMAIL,
    },
)


instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# Middleware'larni qo‘shish
app.add_middleware(LoggingMiddleware)
# app.add_middleware(AuthMiddleware)


# Barcha API marshrutlarini ulaymiz
app.include_router(router)

# Baza mavjud bo‘lmasa, yaratamiz
create_database()


security = HTTPBasic()


# Swagger'ni himoyalash uchun maxsus view yaratamiz
@app.get("/docs", include_in_schema=False)  # Swagger'ni faqat adminlar ko‘rsin
async def get_documentation(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = os.getenv("SWAGGER_AUTH_USERNAME")
    correct_password = os.getenv("SWAGGER_AUTH_PASSWORD")

    if (
        credentials.username != correct_username
        or credentials.password != correct_password
    ):
        raise HTTPException(
            status_code=403, detail="You are not authorized to view this page"
        )

    return get_swagger_ui_html(openapi_url="/openapi.json", title="To-Do API Docs")


@app.get("/", include_in_schema=False)
def root():
    """Root endpoint Swagger'ga yo‘naltiradi"""
    return RedirectResponse(url="/docs")


@app.get("/ping", tags=["Health Check"])
def ping():
    return {"message": f"{settings.PROJECT_NAME} ping!"}

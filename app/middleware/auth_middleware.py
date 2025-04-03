import logging

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

logger = logging.getLogger("uvicorn.access")


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            logger.warning("Unauthorized access attempt.")
            return JSONResponse({"error": "Unauthorized"}, status_code=401)

        return await call_next(request)

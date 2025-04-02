from fastapi import HTTPException
from fastapi.responses import JSONResponse


async def custom_http_exception_handler(request, exc: HTTPException):
    # You can customize the response here
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"Custom message: {exc.detail}"}
    )
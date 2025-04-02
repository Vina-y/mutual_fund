from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def custom_validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for err in exc.errors():
        field = err["loc"][-1]  # Get the field name
        message = err["msg"]  
        errors.append({"field": field, "message": message})

    return JSONResponse(
        status_code=422,
        content={"success": "false", "errors": errors}
    )
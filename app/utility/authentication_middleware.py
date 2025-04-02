from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
import jwt
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response
import os
from dotenv import load_dotenv
load_dotenv()

class AuthenticationMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, secret_key: str):
        super().__init__(app)
        self.secret_key = secret_key
        self.security = HTTPBearer()

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        # List of paths that don't need authentication
        public_paths = [
            "/api/v1/users/login",
            "/api/v1/users/register",
            "/doc",
            "/openapi.json"
        ]

        # Skip authentication for public paths
        if request.url.path in public_paths:
            return await call_next(request)

        try:
            
            auth_header = request.headers.get("Authorization")
            if not auth_header:
                raise HTTPException(status_code=401, detail="No authorization header")

            # Remove 'Bearer ' from the token
            token = auth_header.split(" ")[1]
            payload =  jwt.decode(token, self.secret_key, algorithms=[os.getenv("ALGORITHM")])
            # addin details to user state
            request.state.user = payload
            
            # Continue with the request
            response = await call_next(request)
            return response

        except jwt.ExpiredSignatureError:
            # Token expired error
            return JSONResponse(
                status_code=401,
                content={"detail": "Token has expired"}
            )
        except jwt.InvalidTokenError:
            # Invalid token error
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid token"}
            )
        except Exception as e:
            # General error case
            return JSONResponse(
                status_code=401,
                content={"detail": str(e)}
            )
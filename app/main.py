from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from app.cron_job.scheduler.scheduler import start_scheduler, stop_scheduler
from app.routers import routers
from app.database.db_config import init_db
from app.utility.authentication_middleware import AuthenticationMiddleware
from app.utility.schema_validation_error_handler import custom_validation_exception_handler

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")  # Fallback to default if missing

# Initialize FastAPI App
app = FastAPI(title="Mutual Fund Broker API", docs_url="/doc", openapi_url="/openapi.json")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Database
init_db(app)

#  validation error handler
app.add_exception_handler(RequestValidationError, custom_validation_exception_handler)

# Authentication Middleware
app.add_middleware(AuthenticationMiddleware, secret_key=SECRET_KEY)

app.add_event_handler("startup", start_scheduler)
app.add_event_handler("shutdown", stop_scheduler)

# Include Routes
app.include_router(routers.router)

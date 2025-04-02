# database.py
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI

DATABASE_URL = "sqlite://db.sqlite3"

def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=DATABASE_URL,
        modules={"models": ["app.models.users","app.models.user_purchase_funds"]},  
        generate_schemas=True,  #  generates schemas on startup
        add_exception_handlers=True,  #  exception handlers
    )

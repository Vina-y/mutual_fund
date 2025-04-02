from fastapi import APIRouter
from app.api.v1.user.urls.urls import user_router
from app.api.v1.fund.urls.urls import fund_router

router = APIRouter(prefix="/api/v1",tags=["api"])


# user router
router.include_router(user_router, prefix="/users", tags=["Users"])
router.include_router(fund_router, prefix="/fund", tags=["Funds"])
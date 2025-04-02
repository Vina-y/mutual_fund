from fastapi import APIRouter

from app.api.v1.user.view.login_view.login_view import LoginView
from app.api.v1.user.view.register_user_view.register_user_view import UserRegisterView
# user router 
user_router = APIRouter()

# urls 
user_router.add_api_route("/register", UserRegisterView.register, methods=["POST"])
user_router.add_api_route("/login", LoginView.login, methods=["POST"])
from app.models.users import Users
from app.utility.access_token import create_access_token
from app.utility.hash_password import verify_password


class LoginUser:
    async def login_user(request, login: dict) -> dict:
        try:
            check_user_exist = await Users.get_or_none(email=login.email,status=True)
            if not check_user_exist:
                return False, None,{"credential": "Invalid credentials"}
            
            if not verify_password(login.password, check_user_exist.password):
                return False, None, {"credential": "Invalid credentials"}
            # create token
            token = create_access_token(data={"id": check_user_exist.id})

            return True, {"token": token}, "User loggedIn successfully"
        except Exception as e:
            return False, None, {"error": str(e)}
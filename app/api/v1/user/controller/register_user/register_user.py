from app.models.users import Users
from app.utility.hash_password import hash_password


class RegisterUser:
    async def register_user(request, user: dict) -> dict:
        check_user_exist = await Users.get_or_none(email=user.email)
        if check_user_exist:
            return False, None,{"user_exits": "User already exist"}
        #hash password
        hased_pass = hash_password(user.password)
        # update password with hashed password
        user.password = hased_pass
        user = user.dict(exclude={"confirm_password"})
        # create user
        create_user = await Users.create(**user)

        return True, {"user_id": create_user.id}, "User created successfully"